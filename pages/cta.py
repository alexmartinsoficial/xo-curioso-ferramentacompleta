import streamlit as st

def show_cta():
    """Mostra o CTA de vendas da ferramenta completa"""
    st.markdown('''
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 30px; border-radius: 15px; margin: 30px 0;">
        <h2 style="text-align: center; margin-top: 0; color: white;">🎁 Você desbloqueou apenas 25% da Ferramenta</h2>
        <p style="text-align: center; font-size: 18px; color: white;">
            Você dominou <strong>BUDGET</strong> (Quem tem dinheiro?)<br>
            Mas sem as outras 3 etapas, você ainda vai <strong>perder clientes bons</strong>.
        </p>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("### 🎯 Ferramenta FAROL Completa (4 Etapas):")
    
    st.markdown("**✅ BUDGET:** Quem tem dinheiro? *(Você já treinou isso!)*")
    st.markdown("**🔒 AUTHORITY:** Quem decide de verdade? *(Muitos perdem venda aqui)*")
    st.markdown("**🔒 NEED:** Qual a dor real do cliente? *(Sem isso, ele compra do concorrente)*")
    st.markdown("**🔒 TIMELINE:** Está pronto para fechar AGORA? *(Evita 'vou pensar')*")
    
    st.markdown("---")
    
    st.markdown('''
    <div style="background: #fff3cd; border-left: 5px solid #ffc107; padding: 15px; border-radius: 10px; margin: 20px 0; text-align: center;">
        <p style="color: #856404; margin: 0; font-size: 18px; font-weight: bold;">
            🎁 BÔNUS DISPONÍVEL APENAS HOJE
        </p>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("### 🎁 Bônus Exclusivos:")
    st.markdown("**✅ Scripts prontos** para cada objeção comum")
    st.markdown("**✅ Mapa mental de qualificação** para imprimir")
    st.markdown("**✅ Checklist de atendimento** (nunca mais esqueça de perguntar algo)")
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**Investimento:** Menos que 1 hora do seu tempo com cliente errado")
    
    with col2:
        st.markdown('<div style="text-align: center; font-size: 32px; font-weight: bold; color: #e74c3c; margin-top: 0px;">R$ 27,00</div>', unsafe_allow_html=True)
    
    whatsapp_number = "556232170183"
    whatsapp_message = "Oi! Quero a Ferramenta FAROL Completa (R$ 27)"
    whatsapp_link = f"https://wa.me/{whatsapp_number}?text={whatsapp_message.replace(' ', '%20')}"
    
    st.markdown(f'''
    <div style="text-align: center; margin: 30px 0;">
        <a href="{whatsapp_link}" target="_blank" style="
            background: #e74c3c;
            color: white;
            padding: 15px 40px;
            text-decoration: none;
            border-radius: 50px;
            font-size: 20px;
            font-weight: bold;
            display: inline-block;
            box-shadow: 0 4px 15px rgba(231, 76, 60, 0.4);
        ">
            💬 QUERO OS 100% DA FERRAMENTA - R$ 27
        </a>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('<p style="text-align: center; color: #7f8c8d; font-size: 14px;">Pagamento via PIX • Acesso imediato</p>', unsafe_allow_html=True)
