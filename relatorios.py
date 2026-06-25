import sqlite3


def gerar_relatorio():

    ligacao = sqlite3.connect(
        "batatatracker.db"
    )

    cursor = ligacao.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM encomendas"
    )

    total = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM encomendas
        WHERE estado = 'Entregue'
        """
    )

    entregues = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT SUM(preco)
        FROM encomendas
        WHERE estado = 'Entregue'
        """
    )

    faturacao = cursor.fetchone()[0]

    if faturacao is None:
        faturacao = 0

    print("\n=== RELATÓRIO ===")
    print("Total de encomendas:", total)
    print("Encomendas entregues:", entregues)
    print("Pendentes:", total - entregues)
    print(
        f"Faturação: {faturacao:.2f}€"
    )

    ligacao.close()