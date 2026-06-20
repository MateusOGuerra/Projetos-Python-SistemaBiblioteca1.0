import sqlite3

conexao = sqlite3.connect("biblioteca.db")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM livros")

livros = cursor.fetchall()

for livro in livros:
    print(livro)