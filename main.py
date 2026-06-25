from encomendas import *
from stock import *
from produtos import *
from relatorios import *

while True:

    print("\n=== BATATATRACKER ===")
    print("1 - Nova encomenda")
    print("2 - Ver encomendas")
    print("3 - Alterar estado")
    print("4 - Ver stock")
    print("5 - Atualizar stock")
    print("6 - Ver produtos")
    print("7 - Adicionar produto")
    print("8 - Relatório")
    print("0 - Sair")

    op = input("Opção: ")

    if op == "1":
        criar_encomenda()

    elif op == "2":
        listar_encomendas()

    elif op == "3":
        alterar_estado()

    elif op == "4":
        mostrar_stock()

    elif op == "5":
        atualizar_stock()

    elif op == "6":
        mostrar_produtos()

    elif op == "7":
        adicionar_produto()

    elif op == "8":
        relatorio()

    elif op == "0":
        break