# Código da Aplicação

Esta pasta contém o protótipo funcional do **Templair**, nosso agente de triagem de segurança (SOC).

## Estrutura Atual

Nossa aplicação foi simplificada em um único arquivo principal para facilitar a demonstração no Pitch:

```text
src/
├── app.py              # Aplicação principal (Painel SOC em Streamlit)
├── requirements.txt    # Dependências do projeto (Bibliotecas Python)
└── README.md           # Esta documentação      

Como Rodar a Aplicação
Abra o terminal na raiz do seu repositório e execute os comandos abaixo: 
# 1. Instalar as dependências
pip install -r src/requirements.txt

# 2. Rodar a aplicação do dashboard
streamlit run src/app.py

### 2. Confirme o arquivo `app.py`
Certifique-se de que o arquivo **`app.py`** contém aquele código em Python que eu te enviei na mensagem anterior (começando com `import streamlit as st`). É ele quem vai gerar a interface gráfica quando você rodar o comando `streamlit run src/app.py`.

Fazendo essa troca no texto do `README.md` da pasta `src/`, seu repositório fica 100% livre de qualquer menção a finanças. 

Agora é só rodar no terminal e partir para a gravação do seu vídeo! Deu certo a execução do comando do Streamlit por aí?
