a# 🌱 ColheitaPlus

Sistema interativo para **registro e análise de colheitas de cana-de-açúcar**, com foco em produtividade, eficiência operacional e perdas durante o processo.

---

## 🚀 Objetivo

O objetivo do projeto é oferecer uma solução prática para gerenciamento de operações de colheita, permitindo o acompanhamento de dados como operador, tipo de colheita, máquina utilizada, perdas estimadas e produtividade — tudo com persistência em banco de dados Oracle.

---

## 🔧 Funcionalidades

### 👷 Operadores
- Cadastrar operadores (nome, anos de experiência, tipo de colheita).
- Listar operadores cadastrados.
- Alterar dados de operadores.
- Excluir operadores (exclui também colheitas relacionadas).

### 🚜 Máquinas
- Cadastrar máquinas (modelo, fabricante, ano).
- Listar máquinas.
- Alterar dados de máquinas.
- Excluir máquinas (as colheitas associadas mantêm `id_maquina = NULL`).

### 🌾 Colheitas
- Registrar colheitas com operador, máquina, data, tipo, quantidade e perdas.
  - **Máquina opcional**: Se o usuário não quiser associar uma máquina à colheita, pode inserir `0` no campo `ID da máquina`. O sistema registrará o valor como `NULL`.
  - **Perdas estimadas** são calculadas automaticamente com base no tipo de colheita:
    - **Manual**: 5%.
    - **Mecanizada**: 15%.
- Listar todas as colheitas.
- Alterar colheitas.
- Excluir colheitas.
  - **Cálculo da expectativa**: A expectativa de produção é calculada com base na **média nacional de 77,2 t/ha**.
  - **Status da colheita**:
    - **Dentro da expectativa**: Quando a quantidade colhida é maior ou igual à expectativa.
    - **Abaixo da expectativa**: Quando a quantidade colhida é menor que a expectativa.
- Listar todas as colheitas com o status em relação à expectativa.
- Alterar colheitas.
- Excluir colheitas.

---

## 🗄️ Banco de Dados

- O projeto utiliza **Oracle Database local**.
- A estrutura está definida no arquivo `database/database.sql`.

---

## 📂 Estrutura do Projeto

```
COLHEITAPLUS--MAIN/
├── database/
│   ├── database.sql         # Script de criação das tabelas Oracle
│   └── db_config.py         # Configuração de conexão Oracle
│
├── models/                  # Representações das entidades
│   ├── operador.py
│   ├── maquina.py
│   └── colheita.py
│
├── services/                # Camada de regras de negócio
│   ├── operador_service.py
│   ├── maquina_service.py
│   └── colheita_service.py
│
├── utils/
│   ├── utils.py             # Funções auxiliares
│   └── teste_conexao.py     # Teste de conexão com o Oracle
│
| 
├── main.py                  
└── setup.py                 # Entrada principal do sistema
```

---

## ▶️ Como Executar

1. **Configure o banco de dados:**
   - Instale o Oracle Database localmente.
   - Crie as tabelas com `database/database.sql`.

2. **Edite a conexão no arquivo `db_config.py`:**

```python
import cx_Oracle
dsn = cx_Oracle.makedsn("localhost", "1521", service_name="XE")
conexao = cx_Oracle.connect(user="system", password="123456", dsn=dsn)
```

3. **Execute o sistema:**

```bash
python setup.py
```

---

## 👨‍🏫 Observações

Este projeto foi desenvolvido como atividade prática da disciplina de Python aplicada ao Agronegócio. O foco principal é o uso de estruturas de dados, modularização, funções e banco de dados Oracle.

## Integrantes

 Flavia Nunes Bocchino - RM564213
 Felipe Silva de Menezes - RM557891
 Pedro Henrique Zani - RM564956
 