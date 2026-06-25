from dados import encomendas

def criar_encomenda():

    cliente = input("Cliente: ")
    produto = input("Produto: ")

    nova = {
        "cliente": cliente,
        "produto": produto,
        "estado": "Recebida"
    }

    encomendas.append(nova)

    print("Encomenda criada!")

def listar_encomendas():

    print("\n=== ENCOMENDAS ===")

    if len(encomendas) == 0:
        print("Não existem encomendas.")
        return

    for i, encomenda in enumerate(encomendas):

        print(
            i + 1,
            "-",
            encomenda["cliente"],
            "-",
            encomenda["produto"],
            "-",
            encomenda["estado"]
        )

def alterar_estado():

    listar_encomendas()

    numero = int(input("Número da encomenda: ")) - 1

    if 0 <= numero < len(encomendas):

        print("1 - Em preparação")
        print("2 - Pronta")
        print("3 - Entregue")

        op = input("Novo estado: ")

        if op == "1":
            encomendas[numero]["estado"] = "Em preparação"

        elif op == "2":
            encomendas[numero]["estado"] = "Pronta"

        elif op == "3":
            encomendas[numero]["estado"] = "Entregue"

        print("Estado atualizado!")