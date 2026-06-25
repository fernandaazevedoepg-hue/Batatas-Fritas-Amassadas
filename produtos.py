import sqlite3


def mostrar_produtos():

    ligacao = sqlite3.connect("batatatracker.db")
    cursor = ligacao.cursor()

    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    print("\n=== PRODUTOS ===")

    for produto in produtos:

        print(
            f"{produto[0]} - "
            f"{produto[1]} - "
            f"{produto[2]:.2f}€"
        )

    ligacao.close()


def adicionar_produto():

    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))

    ligacao = sqlite3.connect("batatatracker.db")
    cursor = ligacao.cursor()

    cursor.execute(
        "INSERT INTO produtos(nome, preco) VALUES (?, ?)",
        (nome, preco)
    )

    ligacao.commit()
    ligacao.close()

    print("Produto adicionado!")