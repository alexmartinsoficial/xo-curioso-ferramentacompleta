import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from components.auth import show_login, require_auth, logout
from pages.dashboard import show_dashboard
from components.scenario import Scenario
from components.result import ResultScreen
from pages.home import show_home
from pages.sinais import show_sinais
from pages.cta import show_cta

# Configuração da página
st.set_page_config(
    page_title="Xô Curioso! - Qualificação de Clientes",
    page_icon="🚫",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Google Analytics (executa só 1x)
if 'analytics_loaded' not in st.session_state:
    streamlit_js_eval(js_expressions="""
    (function() {
        var script = document.createElement('script');
        script.async = true;
        script.src = 'https://www.googletagmanager.com/gtag/js?id=G-B5YRT6NE0J';
        document.head.appendChild(script);
        
        script.onload = function() {
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-B5YRT6NE0J', {
                'page_path': window.parent.location.pathname,
                'page_location': window.parent.location.href
            });
        };
    })();
    """, key="analytics")
    st.session_state.analytics_loaded = True

# Carregar CSS
@st.cache_resource
def load_css():
    with open('assets/style.css', 'r', encoding='utf-8') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Inicializar session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Sistema de login
#if not require_auth():
#    show_login()
#    st.stop()

# Adicionar botão de logout no sidebar (quando login estiver ativo)
# with st.sidebar:
#     st.markdown(f"👤 **{st.session_state.get('user_email', 'Usuário')}**")
#     if st.button("🚪 Sair"):
#         logout()

# ==========================================
# ROTEAMENTO DE PÁGINAS
# ==========================================

page = st.session_state.page

# Páginas principais
if page == 'home':
    show_home()

elif page == 'sinais':
    show_sinais()

elif page == 'dashboard':
    show_dashboard()

elif page == 'scenarios':
    st.markdown('<div class="big-title">Escolha um Cenário</div>', unsafe_allow_html=True)
    
    st.markdown('''
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 20px; 
                border-radius: 15px; 
                text-align: center; 
                margin: 20px 0;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);">
        <h3 style="color: white; margin: 0; font-size: 24px;">✨ 3 Situações Reais do Dia a Dia</h3>
    </div>
    ''', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<p style="font-size: 22px; font-weight: bold;">🟢 CENÁRIO 1: MÁRCIA</p>', unsafe_allow_html=True)
        st.markdown("Cliente com orçamento definido. Já pesquisou e quer começar.")
        st.markdown("*Dificuldade: Fácil*")
        if st.button("Começar", key="start_marcia", type="primary", use_container_width=True):
            st.session_state.page = 'scenario_marcia'
            st.rerun()
    
    with col2:
        st.markdown('<p style="font-size: 22px; font-weight: bold;">🟡 CENÁRIO 2: PAULA</p>', unsafe_allow_html=True)
        st.markdown("Interessada mas sem verba. 'Vou ver se consigo juntar...'")
        st.markdown("*Dificuldade: Média*")
        if st.button("Começar", key="start_paula", type="primary", use_container_width=True):
            st.session_state.page = 'scenario_paula'
            st.rerun()
    
    with col3:
        st.markdown('<p style="font-size: 22px; font-weight: bold;">🔴 CENÁRIO 3: CARLA</p>', unsafe_allow_html=True)
        st.markdown("Só pesquisando preços. 'Talvez ano que vem...'")
        st.markdown("*Dificuldade: Difícil*")
        if st.button("Começar", key="start_carla", type="primary", use_container_width=True):
            st.session_state.page = 'scenario_carla'
            st.rerun()
    
    st.markdown("---")
    
    if st.button("⬅️ Voltar para o Início"):
        st.session_state.page = 'home'
        st.rerun()

# Cenários dinâmicos
elif page.startswith('scenario_'):
    scenario_key = page.replace('scenario_', '')
    scenario = Scenario(scenario_key)
    result = scenario.show()
    
    if result == 'result':
        st.session_state.page = f'result_{scenario_key}'
        st.rerun()

# Resultados dinâmicos
elif page.startswith('result_'):
    scenario_key = page.replace('result_', '')
    result_screen = ResultScreen(scenario_key)
    result_screen.show()
    
    st.markdown("---")
    show_cta()

# Página não encontrada
else:
    st.error("❌ Página não encontrada!")
    if st.button("🏠 Voltar ao Início"):
        st.session_state.page = 'home'
        st.rerun()
