#===========Importando json e pandas===========
import json
import pandas as pd
import requests

#===========Importando interface===========
import streamlit as st


#===========Configurando OLLAMA===========
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gemma3:4b"

#===========Carregar dados===========
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv(open('./data/transacoes.csv'))
historico = pd.read_csv(open('./data/historico_atendimento.csv'))
produtos = json.load(open('./data/produtos_financeiros.json'))

#===========Montar contexto===========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

"""

#===========System prompt===========

SYSTEM_PROMPT = """
Você é um agente financeiro inteligente especializado em dívidas, seu nome é EndiviAI.

OBJETIVO:
Seu objetivo é ajudar pessoas com problemas de contas a pagar, estando endividadas. Você deve desvendar soluções para os usuários.

REGRAS:
1. SEMPRE baseie suas respostas nos dados fornecidos
2. NUNCA invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Não responderá assuntos fora de finanças pessoais
5. Não responderá seus usuários de forma rude
6. Não acessará dados bancários de seus usuários
7. Não usará dados fora do contexto
8. Não dará conselhos de apostas ou investimos de alto risco (criptomoedas, ações, derivativos etc)
9. Não faça recomendações de investimento sem perfil do cliente
10. Suas respostas incluem fonte da informação
11. Você se comportará de forma direta e sendo educado
12. O tom de comunicação será formal e acessível
"""

# ==========Chamar Ollama ===========
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    PERGUNTA: {msg}"""

    try:
        r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
        print(f"[DEBUG] Status: {r.status_code}")
        print(f"[DEBUG] Response: {r.text[:500]}")
        
        if not r.ok:
            return f"Erro Ollama ({r.status_code}): {r.text}"
        
        return r.json().get('response', f"Resposta inválida: {r.json()}")
    except Exception as e:
        return f"Erro ao chamar Ollama: {str(e)}"


# ==========Criar interface==========
st.title("EndiviAI - Dívidas e Finanças Pessoais")

if pergunta := st.chat_input("Faça sua pergunta sobre finanças pessoais e dívidas:"):
    st.chat_message("user").write(pergunta)
    with st.spinner("EndiviAI está pensando..."):
        st.chat_message("assistant").write(perguntar(pergunta))