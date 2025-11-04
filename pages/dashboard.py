import streamlit as st

def get_completed_stages():
    """Retorna lista de etapas completadas"""
    completed = []
    
    stages = ['budget', 'authority', 'need', 'timeline']
    
    for stage in stages:
        # Verifica se completou os 3 cenários da etapa (usando nomes corretos do scenarios.json)
        marcia_done = st.session_state.get(f'{stage}_marcia_completed', False)
        paula_done = st.session_state.get(f'{stage}_paula_completed', False)
        carla_done = st.session_state.get(f'{stage}_carla_completed', False)
        
        if marcia_done and paula_done and carla_done:
            completed.append(stage)
    
    return completed

def show_dashboard():
    """Mostra dashboard com progresso das 4 etapas"""
    st.markdown('<div class="big-title">🚦 Seu Progresso no Método FAROL</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin: 20px 0;">
        <p style="font-size: 18px; color: #2c3e50;">
            Bem-vindo(a), <strong>{st.session_state.get('user_email', 'Usuário')}</strong>!<br>
            Complete as 4 etapas para dominar a qualificação de clientes.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Pega etapas completadas
    completed = get_completed_stages()
    progress_percent = (len(completed) / 4) * 100
    
    # Barra de progresso
    st.markdown(f"""
    <div style="background: #f8f9fa; padding: 20px; border-radius: 15px; margin: 20px 0;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <span style="color: #2c3e50; font-weight: bold;">Progresso Geral</span>
            <span style="color: #667eea; font-weight: bold;">{len(completed)}/4 Etapas</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.progress(progress_percent / 100)
    
    st.markdown("---")
    
    # Definir etapas
    stages = [
        {
            'key': 'budget',
            'numero': '1️⃣',
            'titulo': 'Orçamento',
            'subtitulo': '💰 Tem Grana no Bolso?',
            'descricao': 'Identifique quem tem orçamento real'
        },
        {
            'key': 'authority',
            'numero': '2️⃣',
            'titulo': 'Poder de Decisão',
            'subtitulo': '👑 Quem Assina o Cheque?',
            'descricao': 'Descubra quem realmente decide'
        },
        {
            'key': 'need',
            'numero': '3️⃣',
            'titulo': 'Necessidade',
            'subtitulo': '🔥 Dor Real ou Só Olhando?',
            'descricao': 'Encontre a dor verdadeira'
        },
        {
            'key': 'timeline',
            'numero': '4️⃣',
            'titulo': 'Urgência',
            'subtitulo': '⏰ Quer Agora ou 2030?',
            'descricao': 'Crie senso de urgência'
        }
    ]
    
    # Mostrar cards das etapas
    for idx, stage in enumerate(stages):
        is_completed = stage['key'] in completed
        is_locked = idx > 0 and stages[idx-1]['key'] not in completed
        
        # Card da etapa
        if is_completed:
            card_color = "#d4edda"
            border_color = "#28a745"
            icon = "✅"
            button_text = "🔄 Revisar"
            button_type = "secondary"
        elif is_locked:
            card_color = "#f8f9fa"
            border_color = "#ddd"
            icon = "🔒"
            button_text = "🔒 Bloqueado"
            button_type = "secondary"
        else:
            card_color = "#fff3cd"
            border_color = "#ffc107"
            icon = "▶️"
            button_text = "🚀 Começar"
            button_type = "primary"
        
        st.markdown(f"""
        <div style="background: {card_color}; 
                    border-left: 5px solid {border_color}; 
                    padding: 20px; 
                    border-radius: 10px; 
                    margin: 15px 0;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h3 style="margin: 0; color: #2c3e50;">{icon} {stage['numero']} {stage['titulo']}</h3>
                    <p style="margin: 5px 0; color: #667eea; font-size: 18px; font-weight: bold;">{stage['subtitulo']}</p>
                    <p style="margin: 5px 0; color: #7f8c8d;">{stage['descricao']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Botão
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(button_text, 
                        key=f"btn_{stage['key']}", 
                        type=button_type if not is_locked else "secondary",
                        use_container_width=True,
                        disabled=is_locked):
                if not is_locked:
                    st.session_state.page = f"stage_{stage['key']}"
                    st.rerun()
    
    # Se completou tudo, mostrar botão especial
    if len(completed) == 4:
        st.markdown("---")
        st.balloons()
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 30px; 
                    border-radius: 15px; 
                    text-align: center; 
                    margin: 30px 0;">
            <h2 style="color: white; margin: 0;">🎉 PARABÉNS!</h2>
            <p style="color: white; font-size: 18px; margin: 10px 0;">
                Você completou todas as 4 etapas do Método FAROL!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🏆 VER CERTIFICADO E AVALIAR", type="primary", use_container_width=True):
                st.session_state.page = 'conclusao'
                st.rerun()
