import streamlit as st
import pandas as pd
import json
import time

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Templair - SOC Assistant", page_icon="🛡️", layout="wide")
st.title("🛡️ Templair | Assistente de Triagem (SOC)")

# --- CARREGAMENTO DA BASE DE CONHECIMENTO (RAG Simulado) ---
@st.cache_data
def carregar_dados():
    try:
        # Tenta ler os arquivos da pasta data
        df_alertas = pd.read_csv("data/alertas_siem.csv")
        with open("data/politicas_seguranca.json", "r") as f:
            politicas = json.load(f)
        return df_alertas, politicas
    except FileNotFoundError:
        try:
            # Tenta caminho relativo se o comando for executado de dentro da pasta src
            df_alertas = pd.read_csv("../data/alertas_siem.csv")
            with open("../data/politicas_seguranca.json", "r") as f:
                politicas = json.load(f)
            return df_alertas, politicas
        except FileNotFoundError:
            return None, None

df_alertas, politicas = carregar_dados()

# --- BARRA LATERAL (Sidebar) ---
with st.sidebar:
    st.header("⚙️ Painel de Controle")
    st.info("Agente: **Templair** (Blue Team)\nStatus: **Online**")
    
    st.divider()
    st.subheader("📚 Base de Conhecimento RAG")
    if df_alertas is not None:
        st.success("✅ Alertas SIEM carregados")
        st.success("✅ Políticas de Segurança carregadas")
        with st.expander("Ver amostra de logs"):
            st.dataframe(df_alertas.head(2))
    else:
        st.warning("⚠️ Arquivos da pasta 'data/' não encontrados. Verifique a estrutura do projeto.")

# --- HISTÓRICO DE CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá, Analista. Sou o Templair. Cole o log do seu SIEM ou descreva a anomalia na rede para iniciarmos a triagem."}
    ]

# Exibe as mensagens acumuladas no chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- CAIXA DE ENTRADA (Input do usuário) ---
if prompt := st.chat_input("Cole o log de rede ou faça uma pergunta tática..."):
    
    # 1. Registra a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Resposta do Templair
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Respostas para a gravação da demonstração
        if "192.168.1.105" in prompt or "porta: 22" in prompt.lower() or "22" in prompt:
            resposta = "Este log indica uma tentativa de **Força Bruta SSH (Porta 22)** originada do IP `192.168.1.105`.\n\n🛡️ **Ação Imediata recomendada:** Bloqueie o IP no firewall de borda e derrube conexões ativas.\n\nDe acordo com nosso Guia de Mitigação, deseja que eu liste as regras de prevenção a longo prazo (como Fail2Ban)?"
        elif "política" in prompt.lower() or "rdp" in prompt.lower() or "3389" in prompt.lower():
            resposta = "Consultando o arquivo de políticas da `CyberTech Corp`...\n\n⚠️ **Acesso Negado.** De acordo com nossas regras de infraestrutura, as portas 21, 22, 23 e 3389 são bloqueadas na borda. O acesso remoto é permitido **apenas via VPN Corporativa com certificado digital**."
        elif "ransomware" in prompt.lower() or "script" in prompt.lower() or "malware" in prompt.lower():
            resposta = "🛑 **Bloqueio Ético (White Hat):** Como um assistente focado em defesa (Blue Team), não posso gerar payloads ofensivos, malwares ou scripts destrutivos. Posso ajudar explicando como detectar esse tipo de ameaça. Como prefere seguir?"
        else:
            resposta = "Recebi sua solicitação. Para analisar com precisão, preciso de mais detalhes. Você poderia incluir o protocolo, a porta e os IPs de origem/destino envolvidos no alerta?"

        # Efeito visual de digitação
        full_response = ""
        for chunk in resposta.split():
            full_response += chunk + " "
            time.sleep(0.04)
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # 3. Guarda a resposta no histórico do chat
    st.session_state.messages.append({"role": "assistant", "content": full_response})