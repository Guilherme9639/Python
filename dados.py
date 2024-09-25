import sqlite3

conn = sqlite3.connect("Contatos.db")

cursor = conn.cursor()

cursor.execute(''' CREAT_TABLE IF NOT EXISTS Contatos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        e-mail TEXT,
        telefone TEXT
    )
    ''')

dados = [
    ("Guilherme", "cardozoalmeidaguilherme@gmail.com", "(31) 994483976")
    ("Wanessa", "wanealmeida@gmail.com", "(31) 987584899")
    ("Arthur", "arthurar2016@gmail.com", "(31) 9600-8028")
]

cursor.executemany('INSERT INTO Contatos (nome, email, telefone) VALUES (?, ?, ?)', dados)

conn.commit()

cursor.execute('SELECT * FROM Contatos')

contatos = cursor.fetchall()

print("Contatos: ")

for contato in contatos:

    print(contato)

conn.commit()

conn.close()