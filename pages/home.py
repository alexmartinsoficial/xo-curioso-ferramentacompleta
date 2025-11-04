import streamlit as st

def show_home():
    """Mostra a página inicial (capa)"""
    st.markdown('<div class="big-title">🚫 XÔ CURIOSO!</div>', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="subtitle">
        Identifique em 5 minutos quem <strong>TEM DINHEIRO</strong><br>
        e quem só quer <strong>ORÇAMENTO GRÁTIS</strong>.
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('<div class="disclaimer">Não é curso! É um guia prático.</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown('''
    <div class="pain-list">
        <h3 style="margin-top: 0; color: #856404;">Você está cansada de:</h3>
        <div class="pain-item">❌ Perder tempo com "curiosos" que nunca fecham</div>
        <div class="pain-item">❌ Dar desconto por insegurança e desvalorizar seu trabalho</div>
        <div class="pain-item">❌ Agenda cheia mas faturamento baixo</div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="benefits">
        <h3 style="margin-top: 0; color: #0d47a1;">O que você vai aprender:</h3>
        <div class="benefit-item">✅ Identificar em 30 segundos quem tem orçamento real</div>
        <div class="benefit-item">✅ Fazer as perguntas certas sem parecer mercenário</div>
        <div class="benefit-item">✅ Desqualificar clientes errados sem culpa e focar em quem fecha</div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎯 QUERO IDENTIFICAR CLIENTES DE VERDADE", 
                     type="primary", 
                     use_container_width=True):
            st.session_state.page = 'sinais'
            st.rerun()
    
    # FOOTER DENTRO DA FUNÇÃO! ✅
    st.markdown('''
    <div class="footer-info">
        ⚡ Gratuito • 5 minutos • Resultado imediato
    </div>
    ''', unsafe_allow_html=True)
