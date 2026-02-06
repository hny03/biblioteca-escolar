from actions.user_actions import create_user, list_users
from actions.book_actions import create_book, list_books, update_book_quantity
from actions.loan_actions import book_loan, book_return, list_loans

def pause():
    input("\nPressione ENTER para continuar...")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Gerenciar livros")
        print("2. Gerenciar usuários")
        print("3. Empréstimos e Devoluções")
        print("0. Encerrar")

        option = input("Digite o número da ação: ")

        actions = {"1": menu_books, "2": menu_users, "3": menu_loans, "0": None}

        action = actions.get(option)

        if option == "0":
            break

        elif action:
            action()

        else:
            print("❌ Operação inválida")


def menu_books():
    while True:
        print("\n\nGERENCIAR LIVROS 📚")
        print("1. Cadastrar novo livro")
        print("2. Adicionar/Remover livro")
        print("3. Listar todos os livros")
        print("0. Voltar")

        option = input("\nDigite o número da ação: ")

        actions = {
            "1": create_book,
            "2": update_book_quantity,
            "3": list_books,
            "0": lambda: None,
        }

        action = actions.get(option)

        if option == "0":
            break

        elif action:
            action()
            pause()

        else:
            print("❌ Operação inválida")


def menu_users():
    while True:
        print("\n\nGERENCIAR USUÁRIOS 👤")
        print("1. Cadastrar novo usuário")
        print("2. Listar todos os usuários")
        print("0. Voltar")

        option = input("\nDigite o número da ação: ")

        actions = {"1": create_user, 
                   "2": list_users, 
                   "0": lambda: None}

        action = actions.get(option)

        if option == "0":
            break

        elif action:
            action()
            pause()

        else:
            print("❌ Operação inválida")


def menu_loans():
    while True:
        print("\n\nEMPRÉSTIMOS E DEVOLUÇÕES 📝")
        print("1. Registrar empréstimo")
        print("2. Registrar devolução")
        print("3. Listar empréstimos")
        print("0. Voltar")

        option = input("\nDigite o número da ação: ")

        actions = {
            "1": book_loan, 
            "2": book_return, 
            "3": list_loans,
            "0": lambda: None}

        action = actions.get(option)

        if option == "0":
            break

        elif action:
            action()
            pause()

        else:
            print("❌ Operação inválida")


main_menu()
