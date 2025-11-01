import streamlit as st
from components.scenario import Scenario

class ResultScreen:
    def __init__(self, scenario_key):
        """Inicializa tela de resultado para um cenário"""
        self.scenario = Scenario(scenario_key)
        self.score = self.scenario.get_score()
        self.history = self.scenario.get_history()
        self.max_score = len(self.scenario.steps) * 3
        
    def get_classification(self):
        """Retorna classificação baseada na pontuação"""
        # Diferentes mensagens por perfil de cenário
        perfil = self.scenario.perfil
        
        if '🟢' in perfil:  # Verde
            if self.score >= 7:
                return "🟢 EXCELENTE QUALIFICADOR!", "success", "Você domina a arte de qualificar clientes! Sabe fazer as perguntas certas e não desperdiça tempo nem dá descontos desnecessários."
            elif self.score >= 3:
                return "🟡 BOM, MAS PODE MELHORAR", "warning", "Você tem noção básica de qualificação, mas ainda comete erros que podem custar clientes bons ou atrair os ruins."
            else:
                return "🔴 PRECISA TREINAR MAIS", "danger", "Você está perdendo clientes bons e atraindo os ruins. Precisa melhorar urgentemente suas perguntas de qualificação."
        
        elif '🟡' in perfil:  # Amarelo
            if self.score >= 7:
                return "🟢 EXCELENTE! Você sabe lidar com clientes AMARELOS", "success", "Você domina a arte de educar clientes indecisos, criar urgência e não dar descontos desnecessários. Cliente Amarelo nas suas mãos vira Verde!"
            elif self.score >= 3:
                return "🟡 RAZOÁVEL - Precisa melhorar", "warning", "Você até qualifica, mas ainda comete erros que fazem você perder clientes bons ou dar descontos que não precisava."
            else:
                return "🔴 CUIDADO! Você está perdendo dinheiro", "danger", "Cliente Amarelo é quem mais te faz dar desconto ou perder tempo. Você precisa urgentemente melhorar sua qualificação!"
        
        else:  # Vermelho
            if self.score >= 7:
                return "🟢 MESTRE DA DESQUALIFICAÇÃO!", "success", "Você é EXPERT em identificar clientes Vermelhos e não desperdiçar tempo! Sabe quando dizer NÃO sem culpa. Parabéns!"
            elif self.score >= 3:
                return "🟡 AINDA TEM PENA DE DESQUALIFICAR", "warning", "Você identifica cliente Vermelho, mas ainda perde tempo tentando converter. Aprenda a soltar!"
            else:
                return "🔴 VOCÊ É O CLIENTE FAVORITO DOS CURIOSOS", "danger", "Você está perdendo MUITO tempo e dando desconto para quem nunca vai comprar. Urgente rever sua qualificação!"
    
    def get_lesson(self):
        """Retorna lição principal baseada no perfil"""
        perfil = self.scenario.perfil
        
        if '🟢' in perfil:
            return "Cliente Verde já tem orçamento. Foque em criar valor e qualificar urgência, não em dar desconto!"
        elif '🟡' in perfil:
            return "Cliente Amarelo precisa de educação e facilitação (parcelamento), não de desconto! Crie urgência e mostre valor."
        else:
            return "Cliente Vermelho não vira Verde com insistência! Desqualifique sem culpa e preserve sua energia para quem realmente vai comprar."
    
    def show(self):
        """Mostra a tela de resultado"""
        st.markdown('<div class="big-title">🎯 Resultado Final</div>', unsafe_allow_html=True)
        
        classificacao, cor, mensagem = self.get_classification()
        
        st.markdown(f'<div class="score-display" style="font-size: 32px;">{classificacao}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="score-display">Pontuação: {self.score}/{self.max_score} pontos</div>', unsafe_allow_html=True)
        
        if cor == "success":
            st.success(mensagem)
        elif cor == "warning":
            st.warning(mensagem)
        else:
            st.error(mensagem)
        
        st.markdown("---")
        st.markdown("### 🎯 Resumo da sua performance:")
        
        # Contagem de acertos, médias e erros
        total_acertos = sum(1 for item in self.history if item['pontos'] >= 2)
        total_medias = sum(1 for item in self.history if 0 <= item['pontos'] < 2)
        total_erros = sum(1 for item in self.history if item['pontos'] < 0)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("✅ Boas", f"{total_acertos}/{len(self.scenario.steps)}")
        with col2:
            st.metric("⚠️ Médias", f"{total_medias}/{len(self.scenario.steps)}")
        with col3:
            st.metric("❌ Ruins", f"{total_erros}/{len(self.scenario.steps)}")
        
        st.markdown("---")
        st.markdown(f"**💡 LIÇÃO PRINCIPAL:** {self.get_lesson()}")
        
        st.markdown("---")
        st.markdown("### 📝 Revisão das suas escolhas:")
        
        # Mostrar histórico
        for idx, item in enumerate(self.history):
            with st.expander(f"Pergunta {idx + 1} ({item['pontos']:+d} pontos)"):
                st.markdown(f"**Você escolheu:** {item['escolha']}")
                
                # Determinar classe do feedback
                feedback_class = "feedback-warning"
                for opcao in self.scenario.steps[item['step']]['opcoes']:
                    if opcao['texto'] == item['escolha']:
                        feedback_class = f"feedback-{opcao['tipo']}"
                        break
                
                st.markdown(f'<div class="{feedback_class}">{item["feedback"]}</div>', unsafe_allow_html=True)
                st.markdown(f"**Cliente respondeu:** \"{item['resposta']}\"")
                
                # Mostrar resposta ideal
                melhor_opcao = max(self.scenario.steps[item['step']]['opcoes'], key=lambda x: x['pontos'])
                if item['pontos'] < melhor_opcao['pontos']:
                    with st.expander("🎓 Ver a resposta IDEAL"):
                        st.success(f"**Resposta perfeita:** {melhor_opcao['texto']}")
                        st.info(f"**Por quê?** {melhor_opcao['feedback']}")
        
        st.markdown("---")
        
        # CTAs
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Tentar Novamente", use_container_width=True, type="primary"):
                self.scenario.reset()
                st.session_state.page = f'scenario_{self.scenario.key}'
                st.rerun()
        
        with col2:
            if st.button("🏠 Voltar ao Início", use_container_width=True):
                self.scenario.reset()
                st.session_state.page = 'home'
                st.rerun()
