import json
import os

def carregar_dados(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        return []
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
