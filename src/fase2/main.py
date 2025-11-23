from services.operador_service import (
    cadastrar_operador, exibir_operadores, excluir_operador_service, alterar_operador_service
)
from services.maquina_service import (
    cadastrar_maquina, exibir_maquinas, excluir_maquina_service, alterar_maquina_service
)
from services.colheita_service import (
    registrar_colheita, exibir_colheitas, excluir_colheita_service, alterar_colheita_service
)

def menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Menu Operador")
    print("2. Menu Máquina")
    print("3. Menu Colheita")
    print("0. Sair")

def menu_operador():
    print("\n=== MENU OPERADOR ===")
    print("1. Cadastrar Operador")
    print("2. Listar Operadores")
    print("3. Alterar Operador")
    print("4. Excluir Operador")
    print("0. Voltar ao Menu Principal")

def menu_maquina():
    print("\n=== MENU MÁQUINA ===")
    print("1. Cadastrar Máquina")
    print("2. Listar Máquinas")
    print("3. Alterar Máquina")
    print("4. Excluir Máquina")
    print("0. Voltar ao Menu Principal")

def menu_colheita():
    print("\n=== MENU COLHEITA ===")
    print("1. Registrar Colheita")
    print("2. Listar Colheitas")
    print("3. Alterar Colheita")
    print("4. Excluir Colheita")
    print("0. Voltar ao Menu Principal")

def main():
    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                menu_operador()
                opcao_operador = input("Escolha uma opção: ")
                if opcao_operador == "1":
                    cadastrar_operador()
                elif opcao_operador == "2":
                    exibir_operadores()
                elif opcao_operador == "3":
                    alterar_operador_service()
                elif opcao_operador == "4":
                    excluir_operador_service()
                elif opcao_operador == "0":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "2":
            while True:
                menu_maquina()
                opcao_maquina = input("Escolha uma opção: ")
                if opcao_maquina == "1":
                    cadastrar_maquina()
                elif opcao_maquina == "2":
                    exibir_maquinas()
                elif opcao_maquina == "3":
                    alterar_maquina_service()
                elif opcao_maquina == "4":
                    excluir_maquina_service()
                elif opcao_maquina == "0":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "3":
            while True:
                menu_colheita()
                opcao_colheita = input("Escolha uma opção: ")
                if opcao_colheita == "1":
                    registrar_colheita()
                elif opcao_colheita == "2":
                    exibir_colheitas()
                elif opcao_colheita == "3":
                    alterar_colheita_service()
                elif opcao_colheita == "4":
                    excluir_colheita_service()
                elif opcao_colheita == "0":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()