from dados import encomendas

def relatorio():

    total = len(encomendas)

    entregues = 0

    for encomenda in encomendas:

        if encomenda["estado"] == "Entregue":
            entregues += 1

    print("\n=== RELATÓRIO ===")
    print("Total:", total)
    print("Entregues:", entregues)
    print("Pendentes:", total - entregues)