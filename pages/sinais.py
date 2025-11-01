import streamlit as st

def show_sinais():
    """Mostra a explicação dos 3 tipos de cliente"""
    st.markdown('<div class="big-title">🚦 Entenda os 3 Tipos de Cliente</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; font-size: 18px; color: #2c3e50; margin-bottom: 30px;">
        Antes de começar, você precisa entender o <strong>Sistema FAROL de Qualificação</strong>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <h2 style="border-left: 5px solid #f39c12; color: #f39c12; padding-left: 15px; font-size: 22px;">
        Etapa 1 - 💵 Quem tem dinheiro?
    </h2>
    
    <div class="signals-summary">
        <div class="signal-item">
            <span class="signal-item-icon">🟢</span>
            <span class="signal-item-title">Sinal Verde</span>
            <span class="signal-item-text">- Cliente tem orçamento. Avançar!</span>
        </div>
        <div class="signal-item">
            <span class="signal-item-icon">🟡</span>
            <span class="signal-item-title">Sinal Amarelo</span>
            <span class="signal-item-text">- Não possui orçamento, mas pode levantar. Vai te exigir estratégia!</span>
        </div>
        <div class="signal-item">
            <span class="signal-item-icon">🔴</span>
            <span class="signal-item-title">Sinal Vermelho</span>
            <span class="signal-item-text">- Não possui orçamento e não demonstra intenção de investir. Fuja!</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✅ ENTENDI! QUERO TREINAR AGORA", type="primary", use_container_width=True):
            st.session_state.page = 'scenarios'
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("⬅️ Voltar"):
        st.session_state.page = 'home'
        st.rerun()
