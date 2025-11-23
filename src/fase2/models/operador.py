from database.db_config import conectar_banco

def inserir_operador(nome, experiencia, tipo_colheita):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO OPERADOR (nome, experiencia, tipo_colheita)
        VALUES (:nome, :experiencia, :tipo_colheita)
    """, {"nome": nome, "experiencia": experiencia, "tipo_colheita": tipo_colheita})
    conexao.commit()
    conexao.close()

def listar_operadores():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM OPERADOR")
    operadores = cursor.fetchall()
    conexao.close()
    return operadores

def excluir_operador(id_operador):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM OPERADOR WHERE id_operador = :id", {"id": id_operador})
    conexao.commit()
    conexao.close()

def alterar_operador(id_operador, nome, experiencia, tipo_colheita):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Atualize apenas os campos que não são None
    campos = []
    valores = {}

    if nome is not None:
        campos.append("nome = :nome")
        valores["nome"] = nome
    if experiencia is not None:
        campos.append("experiencia = :experiencia")
        valores["experiencia"] = experiencia
    if tipo_colheita is not None:
        campos.append("tipo_colheita = :tipo_colheita")
        valores["tipo_colheita"] = tipo_colheita

    valores["id"] = id_operador

    sql = f"UPDATE OPERADOR SET {', '.join(campos)} WHERE id_operador = :id"
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()