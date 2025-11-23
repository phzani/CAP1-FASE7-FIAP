from models.operador import inserir_operador, listar_operadores, excluir_operador, alterar_operador

def cadastrar_operador():
    nome = input("Nome do operador: ")
    while True:
        try:
            experiencia = int(input("Anos de experiência: "))
            break
        except ValueError:
            print("Erro: Por favor, insira um número válido para a experiência.")
    tipo_colheita = input("Tipo de colheita (manual/mecanizada): ")
    inserir_operador(nome, experiencia, tipo_colheita)
    print("Operador cadastrado com sucesso!")

def exibir_operadores():
    operadores = listar_operadores()
    for operador in operadores:
        print(f"ID: {operador[0]} | Nome: {operador[1]} | Experiência: {operador[2]} anos | Tipo: {operador[3]}")

def excluir_operador_service():
    while True:
        try:
            id_operador = int(input("ID do operador a ser excluído: "))
            excluir_operador(id_operador)
            print("Operador excluído com sucesso!")
            break
        except ValueError:
            print("Erro: Por favor, insira um número válido para o ID.")
        except Exception as e:
            print(f"Erro ao excluir operador: {e}")

def alterar_operador_service():
    try:
        id_operador = int(input("ID do operador a ser alterado: "))
        nome = input("Novo nome do operador (pressione Enter para manter o atual): ")
        experiencia = input("Nova experiência (anos) (pressione Enter para manter o atual): ")
        tipo_colheita = input("Novo tipo de colheita (manual/mecanizada) (pressione Enter para manter o atual): ")

        experiencia = int(experiencia) if experiencia.strip() else None

        alterar_operador(
            id_operador=id_operador,
            nome=nome if nome.strip() else None,
            experiencia=experiencia,
            tipo_colheita=tipo_colheita if tipo_colheita.strip() else None
        )
        print("Operador alterado com sucesso!")
    except ValueError:
        print("Erro: Certifique-se de inserir valores válidos.")
    except Exception as e:
        print(f"Erro ao alterar operador: {e}")