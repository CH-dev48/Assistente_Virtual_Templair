# Base de Conhecimento

## Dados Utilizados

O agente **Templair** utiliza uma base de dados mockada focada 100% em cenários realistas de Cibersegurança e operações de Blue Team. Os arquivos da pasta `data` fornecem o contexto necessário para a triagem:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `alertas_siem.csv` | CSV | Base de logs de tráfego de rede e eventos suspeitos para análise. |
| `guias_mitigacao.json` | JSON | Manual de Playbooks contendo as ações imediatas e prevenções contra ameaças (ex: SQLi, Força Bruta). |
| `historico_incidentes.csv` | CSV | Memória do SOC: contextualiza como a equipe lidou com incidentes semelhantes no passado. |
| `politicas_seguranca.json` | JSON | Define as regras rígidas da infraestrutura (ex: portas bloqueadas, MFA) que o agente não pode violar ao sugerir mitigações. |

> [!TIP]
> **Quer um dataset mais robusto?** Para evoluir o projeto, podem ser integrados datasets públicos do Kaggle ou Hugging Face focados em tráfego de rede, como o *CICIDS2017* ou regras públicas do *Sigma/Snort*.

---

## Adaptações nos Dados

Os dados originais focados no setor financeiro foram totalmente descartados e substituídos por dados de inteligência contra ameaças.
- Criamos amostras de logs estruturados espelhando ferramentas de SIEM padrão.
- Inserimos cenários clássicos de ataques (Exploração Web, Comando e Controle, Reconhecimento) baseados livremente em táticas do framework **MITRE ATT&CK**.
- As políticas de segurança foram desenhadas simulando uma organização de nível intermediário de maturidade (CyberTech Corp) com regras estritas de firewall.

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos JSON e CSV são carregados na memória no início da sessão da aplicação. Eles funcionam como uma base de Consulta Aumentada por Recuperação (RAG simples). 

### Como os dados são usados no prompt?
Quando o analista envia um alerta ou dúvida, a aplicação injeta no `system prompt` as políticas da empresa e o guia de mitigação correspondente ao tipo de ataque detectado. Isso obriga o Templair a basear sua resposta nas regras da CyberTech Corp, evitando que ele "alucine" um procedimento que a empresa não utiliza.

---

## Exemplo de Contexto Montado

Abaixo está um exemplo de como o contexto interno é formatado e enviado para o LLM processar a resposta de forma segura:

```text
[CONTEXTO DE SEGURANÇA DA EMPRESA]
Organização: CyberTech Corp
Política de Acesso Remoto: Permitido apenas via VPN Corporativa com certificado digital.
Diretriz de Incidente: Bloquear IPs externos após 5 tentativas falhas de autenticação em menos de 1 minuto.

[LOG ENVIADO PELO ANALISTA]
2026-07-22 08:15:22 | Origem: 192.168.1.105 | Destino: 10.0.0.50 | Porta: 22
Evento: Múltiplas falhas de login SSH | Severidade: Alta

[INSTRUÇÃO PARA O TEMPLAIR]
Analise o log acima com base nas políticas da empresa e no histórico de incidentes. Sugira a ação imediata de mitigação para o analista, explicando o motivo.
