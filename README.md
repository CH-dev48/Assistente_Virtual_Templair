# 🛡️ Templar AI: Agente de Cibersegurança Inteligente

## Contexto

Os assistentes virtuais no setor de segurança da informação estão evoluindo de simples bases de pesquisa para **agentes inteligentes e proativos**. Neste projeto, o objetivo é idealizar e prototipar um agente de cibersegurança que utiliza IA Generativa para:

- **Acelerar a triagem** de alertas de segurança e logs complexos.
- **Explicar conceitos técnicos** de infraestrutura de redes e vulnerabilidades de forma didática.
- **Guiar investigações** de incidentes de forma consultiva.
- **Garantir a ética e segurança** nas respostas, atuando estritamente sob os princípios de *White Hat* (Defesa e Educação), com barreiras anti-alucinação.

> [!TIP]
> Na pasta [`examples/`](./examples/) você encontra referências de implementação para cada etapa deste desafio.

---

## O Que Você Vai Encontrar Neste Repositório

### 1. Documentação do Agente

Definição de **o que** o agente Sentinel faz e **como** ele funciona:

- **Caso de Uso:** Suporte a analistas de SOC nível 1 e estudantes, ajudando na interpretação de logs (SIEM), cálculos de sub-redes e documentação de testes de invasão.
- **Persona e Tom de Voz:** O agente atua como um mentor técnico experiente: direto, analítico e encorajador.
- **Arquitetura:** Fluxo de ingestão de logs do usuário e cruzamento com a base de conhecimento técnica.
- **Segurança (Guardrails):** Protocolos rígidos para recusar a criação de scripts maliciosos ofensivos, focando apenas em mitigação e defesa.

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Utilização de **dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar e contextualizar o agente:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `alertas_siem.csv` | CSV | Amostras de logs de tráfego e alertas de intrusão |
| `historico_incidentes.csv` | CSV | Casos resolvidos anteriormente (Playbooks) |
| `mitre_attck_subsets.json` | JSON | Táticas e técnicas de ameaças mapeadas |
| `guias_mitigacao.json` | JSON | Políticas de firewall e boas práticas de rede |

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documentação da engenharia de prompts que define as "regras do jogo" para a IA:

- **System Prompt:** Diretrizes de atuação como analista de segurança e restrições éticas fundamentais.
- **Exemplos de Interação (Few-Shot):** Como o agente deve responder ao receber um dump de log confuso.
- **Tratamento de Edge Cases:** Como a IA se comporta quando o usuário pede um exploit funcional ou fornece dados de rede insuficientes.

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

O **protótipo funcional** do agente:

- Interface interativa para o envio de perguntas e logs (Streamlit / Gradio).
- Integração com o LLM.
- Conexão de contexto (RAG - Retrieval-Augmented Generation) com a base de conhecimento.

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Metodologia de avaliação da qualidade e segurança do assistente:

**Métricas Aplicadas:**
- **Precisão Técnica:** Acerto na explicação de conceitos de redes e vulnerabilidades.
- **Taxa de Conformidade Ética:** Percentual de bloqueio bem-sucedido contra requisições maliciosas (Zero alucinação perigosa).
- **Tempo de Resolução:** Redução no tempo de interpretação de um log em comparação com a busca manual.

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Apresentação do projeto (Problema, Solução e Valor):

- Qual gargalo dos centros de operações de segurança o Sentinel resolve?
- Como ele empodera analistas juniores na prática?
- Por que a implementação de IA Generativa com *guardrails* é o futuro da triagem cibernética?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Estrutura do Repositório

```text
📁 assistente-virtual-cybersec/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados e relatórios
│   ├── alertas_siem.csv              # Logs e alertas (CSV)
│   ├── historico_incidentes.csv      # Playbooks de resposta (CSV)
│   ├── mitre_attck_subsets.json      # Táticas de invasão (JSON)
│   └── guias_mitigacao.json          # Regras e mitigação (JSON)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Persona, uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia dos dados (RAG)
│   ├── 03-prompts.md                 # Engenharia de prompts éticos
│   ├── 04-metricas.md                # Avaliação técnica
│   └── 05-pitch.md                   # Roteiro de apresentação
│
├── 📁 src/                           # Código-fonte da aplicação
│   └── app.py                        # Interface do chatbot
│
├── 📁 assets/                        # Diagramas e prints do projeto
│   └── arquitetura_agente.png
│
└── 📁 examples/                      # Referências de implementação
    └── README.md
