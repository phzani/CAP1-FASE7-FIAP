import streamlit as st
import time
import random

def render():
    st.subheader("Monitoramento IoT em Tempo Real")
    
    col1, col2, col3 = st.columns(3)
    
    # Placeholders para métricas
    umidade_ph = col1.empty()
    ph_ph = col2.empty()
    status_bomba = col3.empty()
    
    st.markdown("### Controle Manual")
    if st.button("Ativar Bomba de Irrigação"):
        st.toast("Comando enviado: LIGAR BOMBA")
        time.sleep(1)
        st.success("Bomba ATIVADA")
    
    if st.button("Desativar Bomba"):
        st.toast("Comando enviado: DESLIGAR BOMBA")
        time.sleep(1)
        st.warning("Bomba DESATIVADA")

    st.markdown("---")
    st.markdown("### Leitura de Sensores (Simulação)")
    
    if st.checkbox("Iniciar Monitoramento em Tempo Real"):
        chart_placeholder = st.empty()
        data = []
        
        for i in range(20):
            umidade = random.uniform(40, 90)
            ph = random.uniform(6.0, 7.0)
            
            umidade_ph.metric("Umidade do Solo", f"{umidade:.1f}%", f"{random.uniform(-1, 1):.1f}%")
            ph_ph.metric("pH do Solo", f"{ph:.1f}", f"{random.uniform(-0.1, 0.1):.1f}")
            
            status = "LIGADA" if umidade < 50 else "DESLIGADA"
            status_bomba.metric("Status da Bomba", status)
            
            data.append({"Iteração": i, "Umidade": umidade, "pH": ph})
            chart_placeholder.line_chart(data, x="Iteração", y=["Umidade", "pH"])
            
            # Simulação de Alerta AWS para Umidade Crítica
            if umidade < 45:
                st.toast("⚠️ Umidade Baixa! Verificando necessidade de alerta...")
                if random.random() > 0.8: # Simula envio ocasional para não spammar
                    try:
                        from aws_service.messaging import send_alert_email
                        send_alert_email("Alerta Crítico de Irrigação", f"Umidade do solo crítica ({umidade:.1f}%). Ativação da bomba recomendada.")
                        st.toast("📧 Alerta AWS enviado para a equipe!", icon="☁️")
                    except Exception as e:
                        print(f"Erro envio AWS: {e}")

            time.sleep(0.5)
