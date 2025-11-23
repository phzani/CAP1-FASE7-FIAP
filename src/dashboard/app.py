import streamlit as st
import sys
import os

# Add project root to path to allow imports from other folders
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.set_page_config(page_title="Sistema de Gestão Agrícola", layout="wide")

st.title("🚜 Sistema de Gestão Agrícola Integrado")
st.sidebar.title("Navegação")

page = st.sidebar.radio("Ir para", ["Home", "Fase 1: Planejamento", "Fase 2: Banco de Dados", "Fase 3: Monitoramento IoT", "Fase 4: Machine Learning", "Fase 5: Cloud & Segurança", "Fase 6: Visão Computacional"])

if page == "Home":
    st.markdown("""
    ## Bem-vindo ao Sistema Centralizado
    
    Este dashboard integra todas as fases do projeto de gestão agrícola:
    
    - **Fase 1**: Cálculos de área e dados meteorológicos.
    - **Fase 2**: Gestão de dados estruturados.
    - **Fase 3**: Monitoramento de sensores IoT em tempo real.
    - **Fase 4**: Predição de irrigação com Machine Learning.
    - **Fase 5**: Arquitetura Cloud AWS e Segurança.
    - **Fase 6**: Análise de saúde das plantações com Visão Computacional.
    
    Utilize o menu lateral para navegar entre os módulos.
    """)
    
    st.info("Sistema operando em modo de consolidação (Fase 7).")

elif page == "Fase 1: Planejamento":
    st.header("Fase 1: Planejamento e Meteorologia")
    # Importar e usar lógica da Fase 1 aqui
    try:
        from dashboard.views import fase1_view
        fase1_view.render()
    except ImportError as e:
        st.warning(f"Módulo da Fase 1 ainda não implementado ou não encontrado. Erro: {e}")

elif page == "Fase 2: Banco de Dados":
    st.header("Fase 2: Gestão de Dados")
    try:
        from dashboard.views import fase2_view
        fase2_view.render()
    except ImportError as e:
        st.warning(f"Módulo da Fase 2 ainda não implementado ou não encontrado. Erro: {e}")

elif page == "Fase 3: Monitoramento IoT":
    st.header("Fase 3: Monitoramento IoT")
    try:
        from dashboard.views import fase3_view
        fase3_view.render()
    except ImportError as e:
        st.warning(f"Módulo da Fase 3 ainda não implementado ou não encontrado. Erro: {e}")

elif page == "Fase 4: Machine Learning":
    st.header("Fase 4: Machine Learning")
    try:
        from dashboard.views import fase4_view
        fase4_view.render()
    except ImportError as e:
        st.warning(f"Módulo da Fase 4 ainda não implementado ou não encontrado. Erro: {e}")

elif page == "Fase 5: Cloud & Segurança":
    st.header("Fase 5: Cloud & Segurança")
    try:
        from dashboard.views import fase5_view
        fase5_view.render()
    except ImportError as e:
        st.warning(f"Módulo da Fase 5 ainda não implementado ou não encontrado. Erro: {e}")

elif page == "Fase 6: Visão Computacional":
    st.header("Fase 6: Visão Computacional")
    try:
        from dashboard.views import fase6_view
        fase6_view.render()
    except ImportError as e:
        st.warning(f"Módulo da Fase 6 ainda não implementado ou não encontrado. Erro: {e}")
