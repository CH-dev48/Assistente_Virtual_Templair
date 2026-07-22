# 🛡️ Templair AI: Agente de Cibersegurança Inteligente

## Contexto

Os assistentes virtuais no setor de segurança da informação estão evoluindo de simples bases de pesquisa para **agentes inteligentes e proativos**. Neste projeto, o objetivo é idealizar e prototipar um agente de cibersegurança que utiliza IA Generativa para:

- **Acelerar a triagem** de alertas de segurança e logs complexos.
- **Explicar conceitos técnicos** de infraestrutura de redes e vulnerabilidades de forma didática.
- **Guiar investigações** de incidentes de forma consultiva.
- **Garantir a ética e segurança** nas respostas, atuando estritamente sob os princípios de *White Hat* (Defesa e Educação), com barreiras anti-alucinação.

---

## O Que Você Vai Encontrar Neste Repositório

### 1. Documentação do Agente

Definição do escopo, comportamento e arquitetura do **Templair**:

- **Caso de Uso:** Suporte a analistas de SOC nível 1 e estudantes, ajudando na interpretação de logs (SIEM), cálculos de sub-redes e documentação de incidentes.
- **Persona e Tom de Voz:** O agente atua como um mentor técnico experiente: direto, analítico e encorajador.
- **Arquitetura:** Fluxo de ingestão de logs do usuário e cruzamento com a base de conhecimento técnica.
- **Segurança (Guardrails):** Protocolos rígidos para recusar a criação de scripts maliciosos ofensivos, focando apenas em mitigação e defesa.

📄 **Documentação:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Utilização de **dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar e contextualizar o agente (RAG):

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `alertas_siem.csv` | CSV | Amostras de logs de tráfego de rede e alertas de intrusão |
| `guias_mitigacao.json` | JSON | Playbooks com táticas de ameaças e ações imediatas recomendadas |
| `historico_incidentes.csv` | CSV | Memória de resposta e casos resolvidos anteriormente pela equipe de SOC |
| `politicas_seguranca.json` | JSON | Diretrizes corporativas, regras de firewall e permissões de acesso |

📄 **Documentação:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documentação da engenharia de prompts que define as diretrizes comportamentais da IA:

- **System Prompt:** Regras de atuação como analista de segurança e restrições éticas fundamentais.
- **Exemplos de Interação (Few-Shot):** Exemplos práticos de triagem de logs.
- **Tratamento de Edge Cases:** Comportamento diante de requisições maliciosas ou falta de dados.

📄 **Documentação:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

O **protótipo funcional** do agente e scripts de execução:

- Interface interativa para o envio de perguntas e logs simulando um painel SOC (Streamlit).
- Executável em lote (`executar_templair.bat`) para inicialização com um clique no Windows.

📁 **Pasta da Aplicação:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Metodologia de avaliação da qualidade, segurança e conformidade do assistente.

📄 **Documentação:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Roteiro e apresentação executiva da solução direcionada a gestores de TI e CISOs.

📄 **Documentação:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Estrutura Atual do Repositório

```text
📁 ASSISTENTE_VIRTUAL/
│
├── 📁 assets/                        # Recursos visuais e roteiros auxiliares
│   ├── README.md
│   └── RoteiroLab.md
│
├── 📁 data/                          # Base de dados do SOC (RAG)
│   ├── alertas_siem.csv              # Logs e alertas de rede
│   ├── guias_mitigacao.json          # Playbooks de resposta a incidentes
│   ├── historico_incidentes.csv      # Memória de casos passados
│   └── politicas_seguranca.json      # Regras de infraestrutura e firewall
│
├── 📁 docs/                          # Documentação detalhada do projeto
│   ├── 01-documentacao-agente.md     # Persona, uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados e RAG
│   ├── 03-prompts.md                 # Engenharia de prompts e Guardrails
│   ├── 04-metricas.md                # Avaliação técnica e ética
│   └── 05-pitch.md                   # Roteiro de apresentação executiva
│
├── 📁 examples/                      # Guias de referência e implementação
│   └── README.md
│
├── 📁 src/                           # Código-fonte da aplicação funcional
│   ├── app.py                        # Dashboard interativo do SOC (Streamlit)
│   ├── executar_templair.bat         # Atalho de execução para Windows
│   ├── README.md                     # Instruções do módulo de aplicação
│   └── requirements.txt              # Dependências Python do projeto
│
└── 📄 README.md                      # Documentação principal do repositório



Como Executar o Projeto
Certifique-se de ter o Python instalado na máquina.

Dê dois cliques no arquivo src/executar_templair.bat ou execute no terminal:

Bash
python -m streamlit run src/app.py
