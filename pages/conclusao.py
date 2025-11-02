import streamlit as st
from datetime import datetime

def show_conclusao():
    """Mostra página de conclusão com parabéns e avaliação"""
    
    # Confetes!
    st.balloons()
    
    st.markdown("""
    <div style="text-align: center; margin: 40px 0;">
        <div style="font-size: 80px; margin-bottom: 20px;">🏆</div>
        <h1 style="color: #667eea; font-size: 48px; margin: 0;">PARABÉNS!</h1>
        <p style="font-size: 24px; color: #2c3e50; margin-top: 10px;">
            Você dominou o <strong>Método FAROL Completo</strong>!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Badge de conquista
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 30px; 
                border-radius: 15px; 
                margin: 30px 0;
                text-align: center;">
        <h2 style="color: white; margin: 0;">🎯 Você Agora Domina:</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 20px;">
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px;">
                <div style="font-size: 32px;">💰</div>
                <div style="color: white; font-weight: bold;">Orçamento</div>
                <div style="color: rgba(255,255,255,0.8); font-size: 14px;">Identificar quem tem grana</div>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px;">
                <div style="font-size: 32px;">👑</div>
                <div style="color: white; font-weight: bold;">Decisão</div>
                <div style="color: rgba(255,255,255,0.8); font-size: 14px;">Descobrir quem decide</div>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px;">
                <div style="font-size: 32px;">🔥</div>
                <div style="color: white; font-weight: bold;">Necessidade</div>
                <div style="color: rgba(255,255,255,0.8); font-size: 14px;">Encontrar a dor real</div>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px;">
                <div style="font-size: 32px;">⏰</div>
                <div style="color: white; font-weight: bold;">Urgência</div>
                <div style="color: rgba(255,255,255,0.8); font-size: 14px;">Criar senso de urgência</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Formulário de avaliação
    st.markdown("## 📊 Ajude-nos a melhorar!")
    st.markdown("Sua opinião é muito importante. Todos os campos são **opcionais**.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Seção 1: Antes vs Depois
    st.markdown("### 🔄 Antes vs Depois")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Antes da ferramenta, você:**")
        antes_opcoes = st.multiselect(
            "Selecione todas que se aplicam:",
            [
                "Dava muito desconto",
                "Perdia tempo com curiosos",
                "Não sabia qualificar clientes",
                "Competia só por preço",
                "Fechava pouco"
            ],
            key="antes",
            label_visibility="collapsed"
        )
    
    with col2:
        st.markdown("**Depois da ferramenta, você:**")
        depois_opcoes = st.multiselect(
            "Selecione todas que se aplicam:",
            [
                "Me sinto mais confiante",
                "Sei fazer as perguntas certas",
                "Vou aplicar na prática",
                "Entendo melhor meus clientes",
                "Sei quando desqualificar"
            ],
            key="depois",
            label_visibility="collapsed"
        )
    
    st.markdown("---")
    
    # Seção 2: Aplicação prática
    st.markdown("### 🎯 Aplicação Prática")
    
    col1, col2 = st.columns(2)
    
    with col1:
        vai_aplicar = st.radio(
            "Vai aplicar o método na prática?",
            ["Sim, com certeza!", "Talvez, preciso praticar mais", "Não sei ainda"],
            key="aplicar"
        )
    
    with col2:
        etapa_favorita = st.selectbox(
            "Qual etapa mais te ajudou?",
            ["Orçamento (Tem Grana?)", 
             "Poder de Decisão (Quem Assina?)", 
             "Necessidade (Dor Real?)", 
             "Urgência (Quando?)"],
            key="favorita"
        )
    
    st.markdown("---")
    
    # Seção 3: Avaliação geral
    st.markdown("### ⭐ Avaliação Geral")
    
    nota = st.slider(
        "De 0 a 10, quanto você recomendaria esta ferramenta?",
        0, 10, 8,
        key="nota"
    )
    
    # Feedback visual da nota
    if nota >= 9:
        st.success("🎉 Que ótimo! Muito obrigado pelo feedback!")
    elif nota >= 7:
        st.info("😊 Bacana! O que podemos melhorar?")
    else:
        st.warning("😔 Sentimos muito. Como podemos melhorar?")
    
    st.markdown("---")
    
    # Comentário livre
    st.markdown("### 💬 Comentários (Opcional)")
    comentario = st.text_area(
        "Deixe seu feedback, sugestões ou dúvidas:",
        placeholder="Ex: A ferramenta me ajudou a entender melhor meus clientes...",
        height=100,
        key="comentario"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Botões de ação
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📤 Enviar Avaliação", type="primary", use_container_width=True):
            # Salvar avaliação (você pode conectar com Google Sheets depois)
            avaliacao = {
                'data': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'usuario': st.session_state.get('user_email', 'Anônimo'),
                'antes': antes_opcoes,
                'depois': depois_opcoes,
                'vai_aplicar': vai_aplicar,
                'etapa_favorita': etapa_favorita,
                'nota': nota,
                'comentario': comentario
            }
            
            # Por enquanto, só salva no session_state
            # Depois você pode enviar para Google Sheets ou banco
            st.session_state['avaliacao_enviada'] = avaliacao
            
            st.success("✅ Avaliação enviada com sucesso! Obrigado!")
            st.balloons()
            
            # Aguarda um pouco para mostrar a mensagem
            import time
            time.sleep(2)
            
            # Volta para o dashboard
            st.session_state.page = 'dashboard'
            st.rerun()
    
    with col2:
        if st.button("🏠 Voltar ao Dashboard", use_container_width=True):
            st.session_state.page = 'dashboard'
            st.rerun()
    
    st.markdown("---")
    
    # Mensagem final
    st.markdown("""
    <div style="text-align: center; color: #7f8c8d; margin-top: 30px;">
        <p>💬 Dúvidas ou quer compartilhar seus resultados?</p>
        <a href="https://wa.me/556232170183?text=Completei%20o%20M%C3%A9todo%20FAROL!" 
           target="_blank" 
           style="color: #667eea; text-decoration: none; font-weight: bold;">
            Falar com Jéssica no WhatsApp
        </a>
    </div>
    """, unsafe_allow_html=True)
