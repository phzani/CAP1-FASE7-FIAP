from models.colheita import inserir_colheita, listar_colheitas, excluir_colheita, alterar_colheita
from models.operador import listar_operadores
from models.maquina import listar_maquinas
from datetime import datetime

def registrar_colheita():
    try:
        # Exibir operadores disponíveis
        print("\n=== Operadores Disponíveis ===")
        operadores = listar_operadores()
        for operador in operadores:
            print(f"ID: {operador[0]} | Nome: {operador[1]} | Experiência: {operador[2]} anos | Tipo: {operador[3]}")

        id_operador = int(input("Escolha o ID do operador: "))

        # Exibir máquinas disponíveis
        print("\n=== Máquinas Disponíveis ===")
        maquinas = listar_maquinas()
        for maquina in maquinas:
            print(f"ID: {maquina[0]} | Modelo: {maquina[1]} | Fabricante: {maquina[2]} | Ano: {maquina[3]}")

        id_maquina = int(input("Escolha o ID da máquina (0 se não tiver): "))

        # Determinar o tipo de colheita automaticamente
        if id_maquina == 0:
            tipo_colheita = "manual"
            id_maquina = None  # Tratar como NULL no banco de dados
            perda_estimada = 5.0  # Perda padrão para colheita manual
        else:
            tipo_colheita = "mecanizada"
            perda_estimada = 15.0  # Perda padrão para colheita mecanizada

        area_colhida = float(input("Área colhida (ha): "))
        quantidade_colhida = float(input("Quantidade colhida (t): "))

        # Calcular a quantidade esperada com base na média nacional
        media_nacional = 77.2  # t/ha
        toneladas_esperadas = area_colhida * media_nacional

        # Registrar a colheita no banco de dados
        inserir_colheita(
            id_operador=id_operador,
            id_maquina=id_maquina,
            data_colheita=datetime.now().strftime("%d/%m/%Y"),  # Data atual
            area_colhida=area_colhida,
            tipo_colheita=tipo_colheita,
            quantidade_colhida=quantidade_colhida,
            perda_estimada=perda_estimada
        )
        print("Colheita registrada com sucesso!")
        print(f"Expectativa: {toneladas_esperadas:.2f} t | Colhido: {quantidade_colhida:.2f} t")
    except ValueError:
        print("Erro: Certifique-se de inserir valores válidos.")
    except Exception as e:
        print(f"Erro ao registrar colheita: {e}")

def exibir_colheitas():
    colheitas = listar_colheitas()
    media_nacional = 77.2  # t/ha
    for colheita in colheitas:
        toneladas_esperadas = colheita[5] * media_nacional  # Área colhida * média nacional
        status = "Abaixo da expectativa" if colheita[6] < toneladas_esperadas else "Dentro da expectativa"
        print(f"ID: {colheita[0]} | Operador: {colheita[1]} | Máquina: {colheita[2]} | Tipo: {colheita[3]} | "
              f"Data: {colheita[4]} | Área: {colheita[5]} ha | Quantidade: {colheita[6]:.2f} t | Perda: {colheita[7]}%")
        print(f"  Expectativa comparada a média nacional: {toneladas_esperadas:.2f} t | Status: {status}")

def excluir_colheita_service():
    while True:
        try:
            id_colheita = int(input("ID da colheita a ser excluída: "))
            excluir_colheita(id_colheita)
            print("Colheita excluída com sucesso!")
            break
        except ValueError:
            print("Erro: Por favor, insira um número válido para o ID.")
        except Exception as e:
            print(f"Erro ao excluir colheita: {e}")

def alterar_colheita_service():
    try:
        id_colheita = int(input("ID da colheita a ser alterada: "))
        id_operador = input("Novo ID do operador (pressione Enter para manter o atual): ")
        id_maquina = input("Novo ID da máquina (pressione Enter para manter o atual): ")
        data_colheita = input("Nova data (dd/mm/aaaa) (pressione Enter para manter a atual): ")
        area_colhida = input("Nova área colhida (ha) (pressione Enter para manter a atual): ")
        tipo_colheita = input("Novo tipo de colheita (manual/mecanizada) (pressione Enter para manter a atual): ")
        quantidade_colhida = input("Nova quantidade colhida (t) (pressione Enter para manter a atual): ")
        perda_estimada = input("Nova perda estimada (%) (pressione Enter para manter a atual): ")

        # Converta os valores apenas se o usuário tiver inserido algo
        id_operador = int(id_operador) if id_operador.strip() else None
        id_maquina = int(id_maquina) if id_maquina.strip() else None
        area_colhida = float(area_colhida) if area_colhida.strip() else None
        quantidade_colhida = float(quantidade_colhida) if quantidade_colhida.strip() else None
        perda_estimada = float(perda_estimada) if perda_estimada.strip() else None

        alterar_colheita(
            id_colheita=id_colheita,
            id_operador=id_operador,
            id_maquina=id_maquina,
            data_colheita=data_colheita if data_colheita.strip() else None,
            area_colhida=area_colhida,
            tipo_colheita=tipo_colheita if tipo_colheita.strip() else None,
            quantidade_colhida=quantidade_colhida,
            perda_estimada=perda_estimada
        )
        print("Colheita alterada com sucesso!")
    except ValueError as e:
        print("Erro: Certifique-se de inserir valores válidos.")
    except Exception as e:
        print(f"Erro ao alterar colheita: {e}")