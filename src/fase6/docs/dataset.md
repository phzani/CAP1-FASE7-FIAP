# 📸 Dataset — PBL Fase 6

O conjunto de dados foi criado manualmente utilizando o **MakeSense.ai** e dividido em duas classes principais:

- **Classe A – Desenhos**
- **Classe B – Sofás**

## 🗂 Estrutura de Pastas
📁 A/ → imagens da classe “desenho”
📁 B/ → imagens da classe “sofá”
📁 train/ → arquivos de anotação (.txt) com coordenadas YOLO


Cada arquivo `.txt` contém as coordenadas normalizadas dos objetos detectáveis, no formato YOLO:
<class> <x_center> <y_center> <width> <height>


Exemplo:
0 0.52 0.48 0.31 0.44

## 📷 Exemplos Visuais

**Figura 1 — Classe A (desenhos)**  
![Figura 1](dataset/print_pasta_A.png)

**Figura 2 — Classe B (sofás)**  
![Figura 2](dataset/print_pasta_B.png)

**Figura 3 — Estrutura do diretório “train” com labels YOLO**  
![Figura 3](dataset/print_train_txt.png)

**Figura 4 — Visão geral do dataset completo (A + B)**  
![Figura 4](dataset/print_todos.png)

---

## 💡 Observações
- Total de imagens: **100 (50 por classe)**
- Todas as imagens foram rotuladas manualmente.
- Divisão do dataset: 80% treinamento / 20% validação.
- As classes foram balanceadas para garantir desempenho consistente.
