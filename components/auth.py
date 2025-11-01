import streamlit as st

def check_login(email, password):
    """Verifica se email e senha existem no arquivo users.txt"""
    try:
        with open('users.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if not line:  # Pula linhas vazias
                    continue
                user, pwd = line.split(',')
                if user == email and pwd == password:
                    return True
    except FileNotFoundError:
        st.error("❌ Arquivo de usuários não encontrado!")
        return False
    return False

def show_login():
    """Mostra tela de login"""
    st.markdown('<div class="big-title">🔐 Área de Membros</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <p style="font-size: 18px; color: #2c3e50;">
            Faça login para acessar a ferramenta completa
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        email = st.text_input("📧 Email", placeholder="seu@email.com")
        password = st.text_input("🔑 Senha", type="password", placeholder="••••••••")
        
        if st.button("🚀 Entrar", type="primary", use_container_width=True):
            if not email or not password:
                st.error("❌ Preencha todos os campos!")
            elif check_login(email, password):
                st.session_state.authenticated = True
                st.session_state.user_email = email
                st.success("✅ Login realizado com sucesso!")
                st.rerun()
            else:
                st.error("❌ Email ou senha incorretos!")
        
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #7f8c8d; font-size: 14px;">
            <p>💬 Não tem acesso? Entre em contato via WhatsApp</p>
            <a href="https://wa.me/556232170183?text=Quero%20acesso%20à%20ferramenta" 
               target="_blank" 
               style="color: #667eea; text-decoration: none; font-weight: bold;">
                Falar com Jéssica
            </a>
        </div>
        """, unsafe_allow_html=True)

def logout():
    """Faz logout do usuário"""
    st.session_state.authenticated = False
    st.session_state.user_email = None
    st.rerun()

def require_auth():
    """Verifica se usuário está autenticado"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    return st.session_state.authenticated
