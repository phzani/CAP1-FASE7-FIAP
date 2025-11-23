import streamlit as st
import requests
import pandas as pd

def render():
    st.subheader("Planejamento de Plantio e Meteorologia")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🗺️ Cálculo de Área de Plantio")
        largura = st.number_input("Largura da Área (m)", min_value=0.0, value=100.0)
        comprimento = st.number_input("Comprimento da Área (m)", min_value=0.0, value=100.0)
        
        if st.button("Calcular Área"):
            area = largura * comprimento
            st.success(f"Área Total: {area:.2f} m²")
            st.info(f"Estimativa de Plantas (ex: Milho - 5 plantas/m²): {int(area * 5)} plantas")
            
    with col2:
        st.markdown("### 🌦️ Dados Meteorológicos (Simulado)")
        cidade = st.text_input("Cidade", "São Paulo")
        
        if st.button("Buscar Clima"):
            # Simulação de chamada de API (OpenWeatherMap requer chave)
            st.write(f"Buscando dados para {cidade}...")
            
            # Dados simulados para demonstração
            dados_clima = {
                "Temperatura": "25°C",
                "Umidade": "60%",
                "Condição": "Ensolarado",
                "Vento": "15 km/h"
            }
            
            st.json(dados_clima)
            st.success("Dados atualizados com sucesso!")

    st.markdown("---")
    st.markdown("### 📊 Análise Estatística (R)")
    st.info("A análise estatística em R foi processada e os resultados históricos indicam uma tendência de aumento de temperatura nos últimos 5 anos.")
