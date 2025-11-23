# 🧠 Preparação do Dataset — PBL Fase 6

O dataset foi criado manualmente a partir de imagens coletadas online e rotuladas na plataforma [MakeSense.ai](https://www.makesense.ai/).  
Cada imagem foi classificada em uma das duas categorias:

- **Classe 0:** desenho  
- **Classe 1:** sofá  

Após a rotulagem, os arquivos `.txt` com as anotações foram exportados no formato **YOLOv5** e organizados nas pastas `train/`, `val/` e `test`.

---

## 📂 Estrutura Final do Dataset
datasets/
┣ images/
┃ ┣ train/
┃ ┣ val/
┃ ┗ test/
┣ labels/
┃ ┣ train/
┃ ┣ val/
┃ ┗ test/
┗ dataset.yaml

---

## 🧾 Resumo das Quantidades

| Divisão | Nº de imagens | Descrição |
|----------|----------------|-----------|
| train | 99 | usadas para treino |
| val | 10 | usadas para validação |
| test | 9 | usadas para teste |

---

## 🔗 Conexão com o Colab

As pastas foram sincronizadas no Google Colab com os comandos:

```python
!mkdir /content/datasets
!cp -r /content/drive/MyDrive/PBL6/images /content/datasets/
!cp -r /content/drive/MyDrive/PBL6/labels /content/datasets/

---

## 🧾 Resumo das Quantidades

| Divisão | Nº de imagens | Descrição |
|----------|----------------|-----------|
| train | 99 | usadas para treino |
| val | 10 | usadas para validação |
| test | 9 | usadas para teste |

---

## 🔗 Conexão com o Colab

As pastas foram sincronizadas no Google Colab com os comandos:

```python
!mkdir /content/datasets
!cp -r /content/drive/MyDrive/PBL6/images /content/datasets/
!cp -r /content/drive/MyDrive/PBL6/labels /content/datasets/
O arquivo dataset.yaml foi criado para indicar os caminhos e as classes utilizadas.

👩‍💻 Autores — PBL Fase 6

Flavia Bocchino
Responsável pela estruturação do repositório, criação do dataset, organização das pastas e documentação do projeto.

Pedro Zani
Responsável pelo treinamento do modelo no Google Colab, análise de resultados e ajustes nos hiperparâmetros.

🎓 Instituição: FIAP
📚 Disciplina: Inteligência Artificial
🧩 Professor: (inserir o nome do professor)
📅 Semestre: 2025/2

---

📌 **Commit message (quando clicar em “Commit changes”):**
