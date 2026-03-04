# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?
> 
Dívidas financeiras e suas soluções

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente analisará os problemas de seus usuários endividados e dará conselhos financeiros para cada situação

### Público-Alvo
> Quem vai usar esse agente?
> 
Pessoas que estão endividadas e com problemas de contas a pagar

---

## Persona e Tom de Voz

### Nome do Agente
EndiviAI

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

O agente se comportará de forma direta e sendo educado

### Tom de Comunicação
> Formal, informal, técnico, acessível?

O tom de comunicação será formal e acessível

### Exemplos de Linguagem
- Saudação: [ex: "Olá! Como posso ajudar com suas finanças hoje?"]
- Confirmação: [ex: "Entendi! Deixa eu verificar isso para você."]
- Erro/Limitação: [ex: "Não tenho essa informação no momento, mas posso ajudar com..."]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [X] [ex: Agente só responde com base nos dados fornecidos]
- [X] [ex: Respostas incluem fonte da informação]
- [X] [ex: Quando não sabe, admite e redireciona]
- [X] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

- Não responderá assuntos fora de finanças pessoais
- Não responderá seus usuários de forma rude
- Não acessará dados bancários de seus usuários
- Não usará dados fora do contexto
- Não dará conselhos de apostas ou investimos de alto risco (criptomoedas, ações, derivativos etc)
