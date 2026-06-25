from dados import produtos

def mostrar_produtos():

    print("\n=== PRODUTOS ===")

    for produto in produtos:
        print(
            produto["id"],
            "-",
            produto["nome"],
            "-",
            produto["preco"],
            "€"
        )


def adicionar_produto():

    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))

    novo = {
        "id": len(produtos) + 1,
        "nome": nome,
        "preco": preco
    }

    produtos.append(novo)

    print("Produto adicionado!")