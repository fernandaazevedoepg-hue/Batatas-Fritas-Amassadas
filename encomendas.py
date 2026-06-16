encomendas = []

def criar_encomenda():
    cliente = input("Cliente: ")
    produto = input("Produto: ")

    encomenda = {
        "cliente": cliente,
        "produto": produto,
        "estado": "Recebida"
    }

    encomendas.append(encomenda)

    print("Encomenda criada!")

def listar_encomendas():

    if len(encomendas) == 0:
        print("Sem encomendas.")
        return

    for i in range(len(encomendas)):
        print(
            i + 1,
            encomendas[i]["cliente"],
            encomendas[i]["produto"],
            encomendas[i]["estado"]
        )

def atualizar_estado():

    listar_encomendas()

    indice = int(input("Número da encomenda: ")) - 1

    print("1 - Em preparação")
    print("2 - Pronta")
    print("3 - Entregue")

    op = input("Estado: ")

    if op == "1":
        encomendas[indice]["estado"] = "Em preparação"

    elif op == "2":
        encomendas[indice]["estado"] = "Pronta"

    elif op == "3":
        encomendas[indice]["estado"] = "Entregue"

    print("Estado atualizado!")