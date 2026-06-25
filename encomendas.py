import sqlite3


def criar_encomenda():

    cliente = input("Nome do cliente: ")

    ligacao = sqlite3.connect("batatatracker.db")
    cursor = ligacao.cursor()

    cursor.execute(
        "SELECT * FROM produtos"
    )

    produtos = cursor.fetchall()

    print("\n=== PRODUTOS ===")

    for produto in produtos:

        print(
            f"{produto[0]} - "
            f"{produto[1]} - "
            f"{produto[2]:.2f}€"
        )

    escolha = int(input("\nProduto: "))

    cursor.execute(
        "SELECT nome, preco FROM produtos WHERE id = ?",
        (escolha,)
    )

    produto = cursor.fetchone()

    if produto is None:
        print("Produto inválido.")
        ligacao.close()
        return

    cursor.execute(
        """
        INSERT INTO encomendas
        (cliente, produto, preco, estado)
        VALUES (?, ?, ?, ?)
        """,
        (
            cliente,
            produto[0],
            produto[1],
            "Recebida"
        )
    )

    ligacao.commit()
    ligacao.close()

    print("Encomenda criada!")

def listar_encomendas():

    ligacao = sqlite3.connect("batatatracker.db")
    cursor = ligacao.cursor()

    cursor.execute(
        "SELECT * FROM encomendas"
    )

    encomendas = cursor.fetchall()

    print("\n=== ENCOMENDAS ===")

    if len(encomendas) == 0:
        print("Não existem encomendas.")

    else:

        for encomenda in encomendas:

            print(
                f"{encomenda[0]} - "
                f"{encomenda[1]} - "
                f"{encomenda[2]} - "
                f"{encomenda[3]:.2f}€ - "
                f"{encomenda[4]}"
            )

    ligacao.close()

def alterar_estado():

    listar_encomendas()

    numero = int(
        input("\nID da encomenda: ")
    )

    print("1 - Em preparação")
    print("2 - Pronta")
    print("3 - Entregue")

    op = input("Novo estado: ")

    if op == "1":
        estado = "Em preparação"

    elif op == "2":
        estado = "Pronta"

    elif op == "3":
        estado = "Entregue"

    else:
        print("Opção inválida.")
        return

    ligacao = sqlite3.connect(
        "batatatracker.db"
    )

    cursor = ligacao.cursor()

    cursor.execute(
        """
        UPDATE encomendas
        SET estado = ?
        WHERE id = ?
        """,
        (estado, numero)
    )

    ligacao.commit()
    ligacao.close()

    print("Estado atualizado!")