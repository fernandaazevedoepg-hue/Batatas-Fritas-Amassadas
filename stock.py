from dados import stock

def mostrar_stock():

    print("\n=== STOCK ===")

    for ingrediente in stock:
        print(
            ingrediente,
            "-",
            stock[ingrediente]
        )

def atualizar_stock():

    ingrediente = input("Ingrediente: ")

    if ingrediente in stock:

        quantidade = int(input("Nova quantidade: "))

        stock[ingrediente] = quantidade

        print("Stock atualizado!")

    else:
        print("Ingrediente não encontrado.")

