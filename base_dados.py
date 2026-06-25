import sqlite3

ligacao = sqlite3.connect("batatatracker.db")
cursor = ligacao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS encomendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT NOT NULL,
    produto TEXT NOT NULL,
    preco REAL NOT NULL,
    estado TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingrediente TEXT NOT NULL,
    quantidade INTEGER NOT NULL
)
""")

ligacao.commit()

cursor.execute("SELECT * FROM produtos")

if len(cursor.fetchall()) == 0:

    produtos = [
        ("Batata Simples", 2.50),
        ("Batata com Queijo", 3.50),
        ("Batata com Bacon", 4.00),
        ("Batata Especial", 5.00)
    ]

    cursor.executemany(
        "INSERT INTO produtos(nome, preco) VALUES (?, ?)",
        produtos
    )

cursor.execute("SELECT * FROM stock")

if len(cursor.fetchall()) == 0:

    stock = [
        ("Batatas", 100),
        ("Queijo", 20),
        ("Bacon", 15),
        ("Molho", 30)
    ]

    cursor.executemany(
        "INSERT INTO stock(ingrediente, quantidade) VALUES (?, ?)",
        stock
    )

ligacao.commit()
ligacao.close()