import streamlit as st
import pandas as pd
import numpy as np

def render():
    st.subheader("Gestão de Banco de Dados")
    
    st.markdown("""
    Esta tela permite visualizar os dados armazenados no banco de dados estruturado da Fase 2.
    Como o banco real pode não estar conectado, exibimos uma simulação dos dados.
    """)
    
    # Simulação de dados do banco
    if st.button("Carregar Dados do Banco"):
        # Criar DataFrame simulado
        data = {
            'ID': range(1, 11),
            'Data': pd.date_range(start='2023-01-01', periods=10),
            'Umidade_Solo': np.random.uniform(30, 80, 10),
            'pH': np.random.uniform(5.5, 7.5, 10),
            'Nutriente_P': np.random.choice(['Baixo', 'Adequado'], 10),
            'Nutriente_K': np.random.choice(['Baixo', 'Adequado'], 10)
        }
        df = pd.DataFrame(data)
        
        st.dataframe(df)
        
        st.markdown("### Estatísticas Rápidas")
        col1, col2, col3 = st.columns(3)
        col1.metric("Média Umidade", f"{df['Umidade_Solo'].mean():.1f}%")
        col2.metric("Média pH", f"{df['pH'].mean():.1f}")
        col3.metric("Registros", len(df))
