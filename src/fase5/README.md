# FarmTech Solutions — PBL Fase 4

## Sobre o Projeto
A FarmTech Solutions está prestando serviços de IA para uma fazenda de médio porte (200 hectares) que produz várias culturas. O objetivo é analisar condições de solo e temperatura para prever rendimentos de safra e identificar tendências de produtividade.

**Dataset**: Análise de dados agrícolas incluindo:
- Precipitação (mm/dia)
- Umidade específica e relativa a 2m
- Temperatura a 2m
- Rendimento das culturas (t/ha)

## Funcionalidades Implementadas
1. **Análise Exploratória**: Visualização e compreensão inicial dos dados
2. **Detecção de Outliers**: Usando IQR e IsolationForest
3. **Clusterização**: Identificação de padrões via KMeans
4. **Previsão de Rendimento**: 5 modelos de machine learning implementados:
   - Regressão Linear
   - Ridge
   - Random Forest
   - Gradient Boosting
   - SVR (RBF)

## Integrantes
- Pedro Henrique Zani — RM 564956
- Flavia Nunes Bocchino — RM 564213

## Como Executar o Projeto

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Abra o notebook principal:
```bash
jupyter notebook notebooks/PedroHenriqueZani_rm-564956_and_FlaviaNunesBocchino_rm-564213_pbl_fase4.ipynb
```

> **Importante**: O dataset `crop_yield.csv` já está incluído na pasta `data/`. Execute as células do notebook em ordem para reproduzir as análises.

## Detalhes da Implementação
O notebook contém uma documentação detalhada de cada etapa, incluindo:
- Análise exploratória dos dados agrícolas
- Identificação e tratamento de outliers
- Análise de clusters para identificar padrões
- Implementação e avaliação de 5 modelos preditivos
- Conclusões e limitações do trabalho

## Vídeo Demonstrativo
[Clique aqui para assistir à demonstração](https://youtu.be/51HRzj52Fgw)

## Entrega 2 — Hospedagem em Nuvem (AWS)

# Comparação de Custos AWS (EC2)

## Configuração Utilizada
- **Instância:** t3.micro (2 vCPUs, 1 GiB RAM)  
- **Rede:** até 5 Gbps  
- **Armazenamento:** 50 GB EBS  
- **Sistema Operacional:** Linux  
- **Modelo de preços:** On-Demand (100% utilização mensal)  

---

## Estimativa de Custos

### 📍 Região US East (N. Virginia – EUA)
Virginia: <img width="711" height="588" alt="image" src="https://github.com/user-attachments/assets/ead2ac2b-92ea-42e2-a813-e7d9206f6847" />

- **Custo inicial:** USD 0,00  
- **Custo mensal:** USD 12,03  
- **Custo anual:** USD 144,36  

---

### 📍 Região South America (São Paulo – BR)
SP: <img width="713" height="580" alt="image" src="https://github.com/user-attachments/assets/cece037b-3a83-49b1-9e38-e03237e089d1" />

- **Custo inicial:** USD 0,00  
- **Custo mensal:** USD 1.480,52  
- **Custo anual:** USD 17.766,24  

---

## Comparativo de Custos

| Região           | Custo Mensal (USD) | Custo Anual (USD) |
|------------------|---------------------|-------------------|
| US East (EUA)    | **12,03**           | **144,36**        |
| São Paulo (BR)   | **1.480,52**        | **17.766,24**     |

💡 Diferença de **~147x mais caro** ao escolher São Paulo em vez de Virgínia.

---

## Justificativa Técnica

1. **Acesso rápido aos dados dos sensores**  
   - Se os sensores estiverem no Brasil, usar São Paulo reduz latência de rede.  
   - Mas se a aplicação tolera um pequeno delay (ms a mais), Virgínia pode ser suficiente.  

2. **Restrições legais para armazenamento no exterior**  
   - Caso a legislação ou compliance da empresa exija **dados no território nacional**, a opção **São Paulo** é obrigatória (mesmo com custo elevado).  
   - Se **não houver essa restrição**, a opção **Virgínia** é muito mais viável financeiramente.  

3. **Análise crítica**  
   - **São Paulo**: garante baixa latência local + compliance, mas a um custo proibitivo.  
   - **Virgínia**: entrega os mesmos recursos técnicos por uma fração do preço, com latência ainda aceitável para a maioria dos casos de IoT/telemetria.  

---

## Conclusão

👉 **Opção recomendada:** **US East (Virgínia – EUA)**, salvo se houver **restrição legal** que obrigue armazenar/processar no Brasil.
