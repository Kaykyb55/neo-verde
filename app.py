import streamlit as st
import requests

# Configuração da página
st.set_page_config(
    page_title="Educa.Flowzz v1.1 - AMK",
    page_icon="🤖",
    layout="wide"
)

# CSS personalizado
st.markdown("""
<style>
    .main { background-color: #f0f2f6; }
    .stButton>button { 
        background-color: #1E40AF; 
        color: white; 
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: bold;
    }
    .chat-message { 
        padding: 1rem; 
        border-radius: 0.5rem; 
        margin-bottom: 1rem; 
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .user-message { 
        background-color: #d4edda; 
        border-left: 5px solid #28a745; 
    }
    .bot-message { 
        background-color: #cce5ff; 
        border-left: 5px solid #007bff; 
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://img.icons8.com/clouds/100/artificial-intelligence.png", width=80)
with col2:
    st.title("🤖 EDUCA.FLOWZZ v1.1")
    st.markdown("**IA Educacional Premium - AMK Tecnologia**")
    st.markdown("👨‍💻 Criadores: Kayky & Marcos Luan")

st.markdown("---")

# Função simplificada da IA
def perguntar_ia(pergunta):
    """Respostas educacionais automáticas"""
    respostas = {
        "matematica": "📐 Matemática: Vamos aprender equações e fórmulas!",
        "portugues": "📚 Português: Vamos estudar gramática e literatura!",
        "historia": "🏛️ História: Vamos explorar o passado!",
        "ciencias": "🔬 Ciências: Vamos descobrir o mundo científico!",
        "default": "🤖 Olá! Sou o Educa.Flowzz. Como posso ajudar com suas dúvidas de ensino médio?"
    }
    
    pergunta = pergunta.lower()
    if "matem" in pergunta: return respostas["matematica"]
    if "portug" in pergunta: return respostas["portugues"] 
    if "hist" in pergunta: return respostas["historia"]
    if "cien" in pergunta: return respostas["ciencias"]
    return respostas["default"]

# Histórico de conversa
if "historico" not in st.session_state:
    st.session_state.historico = []

# Área de chat
for mensagem in st.session_state.historico:
    if mensagem["tipo"] == "user":
        st.markdown(f'<div class="chat-message user-message">🎓 <b>Aluno:</b> {mensagem["conteudo"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message bot-message">🤖 <b>Educa.Flowzz:</b> {mensagem["conteudo"]}</div>', unsafe_allow_html=True)

# Input do usuário
pergunta = st.text_input("🎓 Faça sua pergunta:", placeholder="Ex: Explique geometria espacial...", key="input_pergunta")

if st.button("🚀 Enviar Pergunta") and pergunta:
    with st.spinner("💭 Educa.Flowzz processando..."):
        resposta = perguntar_ia(pergunta)
        
        # Adicionar ao histórico
        st.session_state.historico.append({"tipo": "user", "conteudo": pergunta})
        st.session_state.historico.append({"tipo": "bot", "conteudo": resposta})
        
        # Recarregar
        st.rerun()

# Sidebar
with st.sidebar:
    st.header("📚 Sobre o Educa.Flowzz")
    st.markdown("""
    **Versão:** 1.1  
    **Matérias:**  
    - Matemática  
    - Português  
    - História  
    - Ciências
    """)
    
    st.markdown("---")
    st.subheader("🏢 AMK Tecnologia")
    st.markdown("""
    **Criadores:**  
    👨‍💻 Kayky  
    👨‍💻 Marcos Luan
    """)