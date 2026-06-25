import sqlite3


def mostrar_stock():

    ligacao = sqlite3.connect(
        "batatatracker.db"
    )

    cursor = ligacao.cursor()

    cursor.execute(
        "SELECT * FROM stock"
    )

    stock = cursor.fetchall()

    print("\n=== STOCK ===")

    for item in stock:

        print(
            f"{item[1]} - "
            f"{item[2]}"
        )

    ligacao.close()