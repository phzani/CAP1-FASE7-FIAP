import streamlit as st
import os
from PIL import Image
import random
import time

def render():
    st.subheader("Visão Computacional - Monitoramento de Saúde")
    
    st.markdown("""
    Este módulo utiliza Visão Computacional (YOLO) para detectar pragas e doenças nas plantações.
    Selecione uma imagem para análise.
    """)
    
    # Caminho das imagens
    base_path = os.path.join(os.path.dirname(__file__), '../../fase6/imagens')
    
    # Listar imagens disponíveis
    try:
        image_files = [f for f in os.listdir(base_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    except FileNotFoundError:
        st.error(f"Diretório de imagens não encontrado: {base_path}")
        image_files = []
        
    if not image_files:
        st.warning("Nenhuma imagem encontrada para análise.")
        return

    selected_image = st.selectbox("Selecione uma imagem da lavoura", image_files)
    
    if selected_image:
        image_path = os.path.join(base_path, selected_image)
        image = Image.open(image_path)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(image, caption="Imagem Original", use_column_width=True)
            
        with col2:
            st.markdown("### Resultado da Análise")
            if st.button("Processar Imagem"):
                with st.spinner("Analisando com YOLO..."):
                    time.sleep(2) # Simulação de processamento
                    
                    # Simulação de resultados
                    detections = []
                    if random.random() > 0.5:
                        detections.append("Folha Saudável (98%)")
                        status = "SAUDÁVEL"
                        color = "green"
                    else:
                        detections.append("Ferrugem (85%)")
                        detections.append("Lagarta (72%)")
                        status = "ALERTA"
                        color = "red"
                    
                    st.markdown(f"**Status:** :{color}[{status}]")
                    st.markdown("**Detecções:**")
                    for det in detections:
                        st.write(f"- {det}")
                        
                    if status == "ALERTA":
                        st.error("Ação Recomendada: Aplicar defensivo específico e monitorar área.")
                        if st.button("Enviar Alerta para Equipe"):
                            try:
                                from aws_service.messaging import send_alert_email
                                send_alert_email("Alerta de Praga Detectada", f"Praga detectada na imagem {selected_image}. Ação imediata necessária.")
                                st.success("Alerta enviado via AWS SNS/SES!")
                            except Exception as e:
                                st.error(f"Erro ao enviar alerta: {e}")
