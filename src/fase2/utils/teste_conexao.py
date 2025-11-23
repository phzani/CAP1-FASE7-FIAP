from database.db_config import conectar_banco

def testar_conexao():
    try:
        conexao = conectar_banco()
        print("Conexão com o banco de dados estabelecida com sucesso!")
        conexao.close()
    except Exception as e:
        print("Erro ao conectar ao banco de dados:")
        print(e)

if __name__ == "__main__":
    testar_conexao()