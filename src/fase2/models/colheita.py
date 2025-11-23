from database.db_config import conectar_banco

def inserir_colheita(id_operador, id_maquina, data_colheita, area_colhida, tipo_colheita, quantidade_colhida, perda_estimada):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO COLHEITA (id_operador, id_maquina, data_colheita, area_colhida, tipo_colheita, quantidade_colhida, perda_estimada)
        VALUES (:id_operador, :id_maquina, TO_DATE(:data_colheita, 'DD/MM/YYYY'), :area_colhida, :tipo_colheita, :quantidade_colhida, :perda_estimada)
    """, {
        "id_operador": id_operador,
        "id_maquina": id_maquina,
        "data_colheita": data_colheita,
        "area_colhida": area_colhida,
        "tipo_colheita": tipo_colheita,
        "quantidade_colhida": quantidade_colhida,
        "perda_estimada": perda_estimada
    })
    conexao.commit()
    conexao.close()

def listar_colheitas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT c.id_colheita, o.nome, m.modelo, c.tipo_colheita, c.data_colheita, c.area_colhida, c.quantidade_colhida, c.perda_estimada
        FROM COLHEITA c
        LEFT JOIN OPERADOR o ON c.id_operador = o.id_operador
        LEFT JOIN MAQUINA m ON c.id_maquina = m.id_maquina
    """)
    colheitas = cursor.fetchall()
    conexao.close()
    return colheitas

def excluir_colheita(id_colheita):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM COLHEITA WHERE id_colheita = :id", {"id": id_colheita})
    conexao.commit()
    conexao.close()

def alterar_colheita(id_colheita, id_operador, id_maquina, data_colheita, area_colhida, tipo_colheita, quantidade_colhida, perda_estimada):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Atualize apenas os campos que não são None
    campos = []
    valores = {}

    if id_operador is not None:
        campos.append("id_operador = :id_operador")
        valores["id_operador"] = id_operador
    if id_maquina is not None:
        campos.append("id_maquina = :id_maquina")
        valores["id_maquina"] = id_maquina
    if data_colheita is not None:
        campos.append("data_colheita = TO_DATE(:data_colheita, 'DD/MM/YYYY')")
        valores["data_colheita"] = data_colheita
    if area_colhida is not None:
        campos.append("area_colhida = :area_colhida")
        valores["area_colhida"] = area_colhida
    if tipo_colheita is not None:
        campos.append("tipo_colheita = :tipo_colheita")
        valores["tipo_colheita"] = tipo_colheita
    if quantidade_colhida is not None:
        campos.append("quantidade_colhida = :quantidade_colhida")
        valores["quantidade_colhida"] = quantidade_colhida
    if perda_estimada is not None:
        campos.append("perda_estimada = :perda_estimada")
        valores["perda_estimada"] = perda_estimada

    valores["id"] = id_colheita

    sql = f"UPDATE COLHEITA SET {', '.join(campos)} WHERE id_colheita = :id"
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()