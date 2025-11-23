from models.maquina import inserir_maquina, listar_maquinas, excluir_maquina, alterar_maquina

def cadastrar_maquina():
    modelo = input("Modelo da máquina: ")
    fabricante = input("Fabricante: ")
    while True:
        try:
            ano = int(input("Ano: "))
            break
        except ValueError:
            print("Erro: Por favor, insira um número válido para o ano.")
    inserir_maquina(modelo, fabricante, ano)
    print("Máquina cadastrada com sucesso!")

def exibir_maquinas():
    maquinas = listar_maquinas()
    for maquina in maquinas:
        print(f"ID: {maquina[0]} | Modelo: {maquina[1]} | Fabricante: {maquina[2]} | Ano: {maquina[3]}")

def excluir_maquina_service():
    while True:
        try:
            id_maquina = int(input("ID da máquina a ser excluída: "))
            excluir_maquina(id_maquina)
            print("Máquina excluída com sucesso!")
            break
        except ValueError:
            print("Erro: Por favor, insira um número válido para o ID.")
        except Exception as e:
            print(f"Erro ao excluir máquina: {e}")

def alterar_maquina_service():
    try:
        id_maquina = int(input("ID da máquina a ser alterada: "))
        modelo = input("Novo modelo da máquina (pressione Enter para manter o atual): ")
        fabricante = input("Novo fabricante (pressione Enter para manter o atual): ")
        ano = input("Novo ano (pressione Enter para manter o atual): ")

        ano = int(ano) if ano.strip() else None

        alterar_maquina(
            id_maquina=id_maquina,
            modelo=modelo if modelo.strip() else None,
            fabricante=fabricante if fabricante.strip() else None,
            ano=ano
        )
        print("Máquina alterada com sucesso!")
    except ValueError:
        print("Erro: Certifique-se de inserir valores válidos.")
    except Exception as e:
        print(f"Erro ao alterar máquina: {e}")