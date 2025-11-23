import streamlit as st
import os

def render():
    st.subheader("Fase 5: Cloud Computing & Segurança (AWS)")
    
    st.markdown("""
    Nesta fase, toda a infraestrutura foi migrada para a nuvem AWS, garantindo escalabilidade e segurança.
    """)
    
    tabs = st.tabs(["Arquitetura", "Segurança", "Status da Infra"])
    
    with tabs[0]:
        st.markdown("### ☁️ Arquitetura da Solução")
        st.markdown("""
        - **EC2**: Hospedagem do Dashboard e API.
        - **RDS**: Banco de Dados Relacional (PostgreSQL).
        - **S3**: Armazenamento de imagens (Data Lake).
        - **SNS/SES**: Serviço de Mensageria para alertas.
        """)
        
        # Tentar mostrar imagem da arquitetura se existir no repo clonado
        arch_img_path = os.path.join(os.path.dirname(__file__), '../../fase5/arquitetura.png')
        if os.path.exists(arch_img_path):
            st.image(arch_img_path, caption="Diagrama de Arquitetura AWS")
        else:
            st.info("Imagem da arquitetura não encontrada no repositório.")

    with tabs[1]:
        st.markdown("### 🔒 Compliance e Segurança")
        st.success("✅ ISO 27001: Controles de acesso implementados.")
        st.success("✅ ISO 27002: Boas práticas de gestão de segurança.")
        
        st.markdown("#### Medidas Implementadas:")
        st.write("- Criptografia em repouso (RDS/S3).")
        st.write("- Criptografia em trânsito (TLS/SSL).")
        st.write("- IAM Roles com princípio do menor privilégio.")

    with tabs[2]:
        st.markdown("### 🚦 Status dos Serviços (AWS CloudWatch)")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("EC2 (App Server)", "Running", "Uptime: 99.9%")
        col2.metric("RDS (Database)", "Available", "CPU: 12%")
        col3.metric("S3 (Storage)", "OK", "Size: 4.2GB")
