import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()


def cadastrar_livro():

    nome = input("\nDigite o nome do livro: ")

    cursor.execute(
        "INSERT INTO livros(nome, status) VALUES(?, ?)",
        (nome, "Disponível")
    )

    conexao.commit()

    print("Livro cadastrado com sucesso!😊📖")


def listar_livros():

    print("\n=== LIVROS CADASTRADOS ===")

    cursor.execute("SELECT * FROM livros")

    livros = cursor.fetchall()

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")

    else:

        for livro in livros:
            print(f"{livro[0]} - {livro[1]} ({livro[2]})")


def pesquisar_livro():

    nome = input("\nDigite o nome do livro: ")

    cursor.execute(
        "SELECT * FROM livros WHERE nome = ?",
        (nome,)
    )

    livro = cursor.fetchone()

    if livro:
        print("\nLivro encontrado!😃")

    else:
        print("\nLivro não encontrado.😞")


def remover_livro():

    nome = input("\nDigite o nome do livro para remover: ")

    cursor.execute(
        "DELETE FROM livros WHERE nome = ?",
        (nome,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("\nLivro removido com sucesso!😁")

    else:
        print("\nLivro não encontrado.😞")

def emprestar_livro():

    nome = input("\nDigite o nome do livro: ")

    cursor.execute(
        "UPDATE livros SET status = 'Emprestado' WHERE nome = ?",
        (nome,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("\nLivro emprestado!😊")

    else:
        print("\nLivro não encontrado.😞")

def devolver_livro():

    nome = input("\nDigite o nome do livro: ")

    cursor.execute(
        "UPDATE livros SET status = 'Disponível' WHERE nome = ?",
        (nome,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("\nLivro devolvido!")

    else:
        print("\nLivro não encontrado.😞")

def menu():

    while True:

        print("\n=== SISTEMA DE BIBLIOTECA📚 ===")
        print("1 - Cadastrar Livro📝")
        print("2 - Listar Livros📋")
        print("3 - Pesquisar Livro🔎")
        print("4 - Remover Livro 🗑️")
        print("5 - Emprestar Livro 📚")
        print("6 - Devolver Livro 📖")
        print("7 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()

        elif opcao == "2":
            listar_livros()

        elif opcao == "3":
            pesquisar_livro()

        elif opcao == "4":
            remover_livro()

        elif opcao == "5":
            emprestar_livro()

        elif opcao == "6":
            devolver_livro()

        elif opcao == "7":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida!")


menu()