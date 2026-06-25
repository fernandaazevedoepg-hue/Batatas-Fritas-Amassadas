from encomendas import encomendas


def gerar_relatorio():


    print("\n=== RELATÓRIO ===")


    print("Total de encomendas:", len(encomendas))


    entregues = 0


    for encomenda in encomendas:


        if encomenda["estado"] == "Entregue":
            entregues += 1


    print("Entregues:", entregues)

