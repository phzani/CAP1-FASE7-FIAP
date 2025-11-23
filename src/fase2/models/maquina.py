from database.db_config import conectar_banco

def inserir_maquina(modelo, fabricante, ano):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO MAQUINA (modelo, fabricante, ano)
        VALUES (:modelo, :fabricante, :ano)
    """, {"modelo": modelo, "fabricante": fabricante, "ano": ano})
    conexao.commit()
    conexao.close()

def listar_maquinas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM MAQUINA")
    maquinas = cursor.fetchall()
    conexao.close()
    return maquinas

def excluir_maquina(id_maquina):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM MAQUINA WHERE id_maquina = :id", {"id": id_maquina})
    conexao.commit()
    conexao.close()

def alterar_maquina(id_maquina, modelo, fabricante, ano):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Atualize apenas os campos que não são None
    campos = []
    valores = {}

    if modelo is not None:
        campos.append("modelo = :modelo")
        valores["modelo"] = modelo
    if fabricante is not None:
        campos.append("fabricante = :fabricante")
        valores["fabricante"] = fabricante
    if ano is not None:
        campos.append("ano = :ano")
        valores["ano"] = ano

    valores["id"] = id_maquina

    sql = f"UPDATE MAQUINA SET {', '.join(campos)} WHERE id_maquina = :id"
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()