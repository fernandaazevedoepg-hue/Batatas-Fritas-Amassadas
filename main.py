import os
import base_dados

from encomendas import *
from produtos import *
from stock import *
from relatorios import *


def limpar():
    os.system(
        "cls" if os.name == "nt"
        else "clear"
    )


while True:

    limpar()

    print("================================")
    print("          BATATA TRACKER")
    print("================================")
    print("1 - Nova encomenda")
    print("2 - Ver encomendas")
    print("3 - Alterar estado")
    print("4 - Ver stock")
    print("5 - Ver produtos")
    print("6 - Adicionar produto")
    print("7 - Relatório")
    print("0 - Sair")

    opcao = input(
        "\nEscolha uma opção: "
    )

    if opcao == "1":
        limpar()
        criar_encomenda()

    elif opcao == "2":
        limpar()
        listar_encomendas()

    elif opcao == "3":
        limpar()
        alterar_estado()

    elif opcao == "4":
        limpar()
        mostrar_stock()

    elif opcao == "5":
        limpar()
        mostrar_produtos()

    elif opcao == "6":
        limpar()
        adicionar_produto()

    elif opcao == "7":
        limpar()
        gerar_relatorio()

    elif opcao == "0":
        break

    input(
        "\nPrima ENTER para continuar..."
    )