# 🧠 PBL Fase 6 — Detecção de Objetos (Desenhos × Sofás)

Projeto da Fase 6 (IA / FIAP): detector de objetos com **YOLOv5**, usando dataset próprio (MakeSense) e experimento **“ir além”** com **Transfer Learning (Keras)**.

🎥 [Apresentação no YouTube](https://youtu.be/ue7RudZGxT0)

---

## 🎯 Objetivo

Treinar um modelo que identifique **duas classes**:

| Classe | Nome     |
|:------:|-----------|
| 0 | Desenho |
| 1 | Sofá |

Dataset rotulado manualmente.  
Treino principal em **Google Colab com YOLOv5**, e extensão com **MobileNetV2 / TensorFlow**.

---

## 📂 Estrutura

| Tipo | Caminho | Descrição |
|------|----------|------------|
| 🧩 Modelo | `best.pt` | Modelo final YOLOv5 |
| 🖼️ Imagens | `imagens/` | Originais A_*.jpg (Desenhos) e B_*.jpg (Sofás) |
| 📝 Rótulos | `artefatos/` | Anotações YOLO exportadas do MakeSense |
| 📄 Documentos | `docs/` | Dataset e autores |
| 📓 Notebooks | `notebooks/` | YOLOv5 + Transfer Learning |

---

## ⚙️ Reproduzir treino (Colab)

1️⃣ Ative GPU → *Ambiente de execução → Alterar tipo → GPU*  
2️⃣ Instale YOLOv5:  
```bash
!git clone https://github.com/ultralytics/yolov5
%cd yolov5
%pip install -r requirements.txt
!git clone https://github.com/<USUARIO>/pbl_fase6_FlaviaBocchino---PedroZani.git

4️⃣ Treine (30 épocas, batch 16):

!python train.py --img 640 --batch 16 --epochs 30 \
  --data /content/datasets/dataset.yaml \
  --weights yolov5s.pt --name treino_repo


📈 Resultados: runs/train/treino_repo/ → best.pt, results.png, confusion_matrix.png
▶️ Inferência
!python detect.py --weights /content/best.pt \
  --img 640 --conf 0.25 \
  --source /content/pbl_fase6_FlaviaBocchino---PedroZani/imagens


🖼️ Saída: runs/detect/exp*/
📊 Resultados

results.png: curvas de loss, precision, recall, mAP.

confusion_matrix.png: alta precisão (~1.0) e recall próximo de 1.0.

Excelente desempenho na distinção entre desenho e sofá.
🚀 Ir Além — Transfer Learning

Notebook PBL_Fase6_IrAlem_TransferLearning.ipynb:

Base: MobileNetV2 / TensorFlow

Divide train/val, treina e gera classification_report

Mostra matriz de confusão com resultados equivalentes ao YOLOv5
👩‍💻 Autores
Nome	RM
Flavia Bocchino	564213
Pedro Zani	564956
🧠 Obs.: arquivos grandes (ex: best.pt) podem mostrar “We can’t show files that are this big”. É normal. Baixe o arquivo e carregue no Colab.
