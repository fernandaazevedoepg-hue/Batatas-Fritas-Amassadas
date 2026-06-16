stock = {
    "Batatas": 100,
    "Queijo": 20,
    "Bacon": 15,
    "Molho": 30
}


def mostrar_stock():


    print("\n=== STOCK ===")


    for item in stock:
        print(item, "-", stock[item])

