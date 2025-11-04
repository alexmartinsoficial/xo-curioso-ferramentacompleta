import streamlit as st
import json
import time

class Scenario:
    def __init__(self, scenario_key):
        """Carrega cenário do JSON"""
        self.key = scenario_key
        self.data = self.load_scenario_data()
        self.nome = self.data['nome']
        self.perfil = self.data['perfil']
        self.contexto = self.data['contexto']
        self.steps = self.data['steps']
        
    @staticmethod
    def load_scenarios():
        """Carrega todos cenários dos 4 arquivos JSON (com cache)"""
        all_scenarios = {}
        
        # Lista dos 4 arquivos JSON
        json_files = ['budget', 'authority', 'need', 'timeline']
        
        for file in json_files:
            try:
                with open(f'data/scenarios_{file}.json', 'r', encoding='utf-8') as f:
                    scenarios = json.load(f)
                    all_scenarios.update(scenarios)
            except FileNotFoundError:
                st.error(f"❌ Arquivo scenarios_{file}.json não encontrado!")
            except json.JSONDecodeError as e:
                st.error(f"❌ Erro ao ler scenarios_{file}.json: {e}")
        
        return all_scenarios
    
    def load_scenario_data(self):
        """Carrega dados específicos do cenário"""
        scenarios = self.load_scenarios()
        
        if self.key not in scenarios:
            st.error(f"❌ Cenário '{self.key}' não encontrado!")
            st.stop()
            
        return scenarios[self.key]
    
    def init_state(self):
        """Inicializa session state para este cenário"""
        if f'{self.key}_step' not in st.session_state:
            st.session_state[f'{self.key}_step'] = 0
        if f'{self.key}_score' not in st.session_state:
            st.session_state[f'{self.key}_score'] = 0
        if f'{self.key}_history' not in st.session_state:
            st.session_state[f'{self.key}_history'] = []
    
    def reset(self):
        """Reseta o cenário"""
        st.session_state[f'{self.key}_step'] = 0
        st.session_state[f'{self.key}_score'] = 0
        st.session_state[f'{self.key}_history'] = []
        if f'{self.key}_show_continue' in st.session_state:
            del st.session_state[f'{self.key}_show_continue']
    
    def get_current_step(self):
        """Retorna step atual"""
        return st.session_state[f'{self.key}_step']
    
    def get_score(self):
        """Retorna pontuação"""
        return st.session_state[f'{self.key}_score']
    
    def get_history(self):
        """Retorna histórico"""
        return st.session_state[f'{self.key}_history']
    
    def show(self):
        """Mostra o cenário interativo"""
        self.init_state()
        current_step = self.get_current_step()
        
        # Cabeçalho
        st.markdown(f'<div class="big-title">📱 Cenário: {self.nome}</div>', unsafe_allow_html=True)
        st.markdown(f'**Perfil:** {self.perfil}')
        
        # Contexto (só no início)
        if current_step == 0:
            st.info(self.contexto)
            st.markdown("---")
        
        # Mostrar pontuação e progresso
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'<div class="score-display">📊 Pontos: {self.get_score()}</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="score-display">🎯 Pergunta: {current_step + 1}/{len(self.steps)}</div>', unsafe_allow_html=True)
        
        # Barra de progresso
        progress = (current_step / len(self.steps)) * 100
        st.progress(progress / 100)
        
        st.markdown("---")
        
        # Verificar se acabou
        if current_step >= len(self.steps):
            return 'result'  # Sinaliza que deve mostrar resultado
        
        # Pegar step atual
        step_data = self.steps[current_step]
        
        # Mostrar fala da cliente
        st.markdown(f'''
        <div class="cliente-bubble">
            <strong>💬 {self.nome} diz:</strong><br>
            "{step_data["cliente_fala"]}"
        </div>
        ''', unsafe_allow_html=True)
        
        # Se já mostrou feedback, mostra botão continuar
        if st.session_state.get(f'{self.key}_show_continue', False):
            # Pega último item do histórico para mostrar feedback
            last_choice = self.get_history()[-1]
            
            # Mostra feedback novamente
            if last_choice['pontos'] >= 2:
                st.success(f"✅ {last_choice['feedback']}")
                st.info(f"💬 **{self.nome} responde:** {last_choice['resposta']}")
            elif last_choice['pontos'] >= 0:
                st.warning(f"⚠️ {last_choice['feedback']}")
                st.info(f"💬 **{self.nome} responde:** {last_choice['resposta']}")
            else:
                st.error(f"❌ {last_choice['feedback']}")
                st.info(f"💬 **{self.nome} responde:** {last_choice['resposta']}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("➡️ Próxima Pergunta", type="primary", key=f"continue_{self.key}_{current_step}"):
                st.session_state[f'{self.key}_show_continue'] = False
                st.rerun()
            
            st.stop()  # Para não mostrar as opções novamente
        
        st.markdown("### Como você responde?")
        
        # Mostrar opções
        for idx, opcao in enumerate(step_data['opcoes']):
            letra = chr(65 + idx)  # A, B, C, D
            if st.button(f"{letra}) {opcao['texto']}", key=f"opt_{self.key}_{current_step}_{idx}", use_container_width=True):
                # Registrar escolha PRIMEIRO
                st.session_state[f'{self.key}_history'].append({
                    'step': current_step,
                    'escolha': opcao['texto'],
                    'pontos': opcao['pontos'],
                    'feedback': opcao['feedback'],
                    'resposta': opcao['resposta_cliente']
                })
                st.session_state[f'{self.key}_score'] += opcao['pontos']
                st.session_state[f'{self.key}_step'] += 1
                
                # Marca para mostrar o botão continuar
                st.session_state[f'{self.key}_show_continue'] = True
                st.rerun()
        
        st.markdown("---")
        
        # Botão voltar
        if st.button("⬅️ Voltar para Cenários"):
            self.reset()
            st.session_state.page = 'scenarios'
            st.rerun()
        
        return 'running'  # Cenário ainda está rodando
