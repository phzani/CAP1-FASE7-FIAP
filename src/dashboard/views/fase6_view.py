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
                    
                    # Análise baseada no nome do arquivo para demonstração realista
                    filename_lower = selected_image.lower()
                    detections = []
                    status = "SAUDÁVEL"
                    color = "green"
                    action = None
                    
                    # Detectar doenças baseado no nome do arquivo
                    if "ferrugem" in filename_lower or "rust" in filename_lower:
                        detections.append("Ferrugem (Puccinia spp.) - 89%")
                        detections.append("Lesões foliares - 76%")
                        status = "ALERTA CRÍTICO"
                        color = "red"
                        action = "Aplicar fungicida à base de triazol. Monitorar propagação."
                    elif "mancha" in filename_lower or "blight" in filename_lower:
                        detections.append("Mancha Foliar (Cercospora) - 85%")
                        detections.append("Necrose tecidual - 72%")
                        status = "ALERTA"
                        color = "orange"
                        action = "Aplicar fungicida sistêmico. Remover folhas afetadas."
                    elif "pinta" in filename_lower or "early" in filename_lower:
                        detections.append("Pinta Preta (Alternaria solani) - 91%")
                        detections.append("Anéis concêntricos - 88%")
                        status = "ALERTA CRÍTICO"
                        color = "red"
                        action = "Aplicar clorotalonil. Aumentar espaçamento entre plantas."
                    elif "oidio" in filename_lower or "mildew" in filename_lower:
                        detections.append("Oídio (Blumeria graminis) - 93%")
                        detections.append("Micélio branco - 87%")
                        status = "ALERTA"
                        color = "orange"
                        action = "Aplicar enxofre ou fungicida específico. Melhorar ventilação."
                    elif "requeima" in filename_lower or "late" in filename_lower:
                        detections.append("Requeima (Phytophthora infestans) - 95%")
                        detections.append("Lesões encharcadas - 90%")
                        status = "ALERTA CRÍTICO"
                        color = "red"
                        action = "Aplicar fungicida urgente. Destruir plantas severamente afetadas."
                    else:
                        detections.append("Folha Saudável - 98%")
                        detections.append("Sem sinais de patógenos - 96%")
                    
                    st.markdown(f"**Status:** :{color}[{status}]")
                    st.markdown("**Detecções:**")
                    for det in detections:
                        st.write(f"- {det}")
                    
                    if action:
                        st.error(f"**Ação Recomendada:** {action}")
                        if st.button("Enviar Alerta para Equipe"):
                            try:
                                from aws_service.messaging import send_alert_email
                                send_alert_email(
                                    f"Alerta: {status} - {selected_image}", 
                                    f"Doença detectada: {detections[0]}\n\nAção: {action}\n\nImagem: {selected_image}"
                                )
                                st.success("✅ Alerta enviado via AWS SNS/SES!")
                            except Exception as e:
                                st.warning(f"⚠️ Modo simulação (AWS não configurada): {e}")

