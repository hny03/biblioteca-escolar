from models import Loan
from actions.user_actions import get_user_by_id
from actions.book_actions import get_book_by_code, update_book_quantity
import csv
import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
FILE_PATH_LOANS = BASE_DIR / "data" / "loans.csv"


def load_loans():
    loans = []

    if not os.path.exists(FILE_PATH_LOANS):
        print("Nenhum empréstimo registrado ainda.")
        return loans

    with open(FILE_PATH_LOANS, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            loan = Loan(
                row["id"],
                row["book"],
                row["user"],
                row["loan_date"],
                row["return_date"],
                row["status"],
            )

            loans.append(loan)

        return loans

# id, book, user, loan_date, return_date, status

def save_loans(Loans):
        with open(FILE_PATH_LOANS, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "book", "user", "loan_date", "return_date", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for loan in Loans:
                writer.writerow({
                    "id": loan.id,
                    "book": loan.book,
                    "user": loan.user,
                    "loan_date": loan.loan_date,
                    "return_date": loan.return_date,
                    "status": loan.status
                })

def book_loan():
        
    print("\n\nRegistrando empréstimo...\n")
    book = input("Digite o ID do livro: ")
    
    book_obj = get_book_by_code(int(book))
    
    if not book_obj:
        print("🧐 Livro não encontrado!")
        return
    
    if book_obj.disponibility == False:
        print("❌ Livro indisponível para empréstimo!")
        return
    
    user = input("Digite o ID do usuário: ")
    
    user_obj = get_user_by_id(int(user))
    if not user_obj:
        print("🧐 Usuário não encontrado!")
        return
    
    loan_date = input("Digite a data do empréstimo (DD/MM/AAAA): ")
    return_date = input("Digite a data de devolução (DD/MM/AAAA): ")

    update_book_quantity(int(book), -1)
    
    status = "ativo"

    new_loan = Loan(
        id=str(len(load_loans()) + 1),
        book=book,
        user=user,
        loan_date=loan_date,
        return_date=return_date,
        status=status
    )
    
    loans = load_loans()
    loans.append(new_loan)
    save_loans(loans)
    
    print("✔️ Empréstimo registrado com sucesso!")

def list_loans():
    
    print("\n\nListando empréstimos...")
    loans = load_loans()

    if not loans:
        print("Nenhum empréstimo registrado.")
        return
    
    
    choice = input("a. Listar todos os empréstimos\nb. Listar apenas empréstimos ativos\nc. Listar empréstimos de um usuário\n\nDigite a letra da opção desejada: ")
    
    if(choice == "c"):
        user_id = input("Digite o ID do usuário: ")
        user = get_user_by_id(int(user_id))
        if not user:
            print("🧐 Usuário não encontrado!")
            return

    for loan in loans:
        if choice == "c":
            if int(loan.user) == int(user_id):
                print(f"ID: {loan.id} | Livro: {get_book_by_code(int(loan.book)).title} (#{loan.book}) | Usuário: {user.name} (#{user_id}) | Data do Empréstimo: {loan.loan_date} | Data de Devolução: {loan.return_date} | Status: {loan.status}")
        elif choice == "b" and loan.status == "ativo":
            print(f"ID: {loan.id} | Livro: {loan.book} | Usuário: {loan.user} | Data do Empréstimo: {loan.loan_date} | Data de Devolução: {loan.return_date} | Status: {loan.status}")
        elif choice == "a":
            print(f"ID: {loan.id} | Livro: {get_book_by_code(int(loan.book)).title} (#{loan.book}) | Usuário: {get_user_by_id(int(loan.user)).name} (#{loan.user}) | Data do Empréstimo: {loan.loan_date} | Data de Devolução: {loan.return_date} | Status: {loan.status}")

def book_return():
    print("\n\nRegistrar devolução...\n")
    loan_id = input("Digite o ID do empréstimo a ser fechado: ")
    
    loans = load_loans()
  
    for loan in loans:
        if int(loan.id) == int(loan_id):
            Loan.change_status(loan, "fechado")
            book_id = int(loan.book)
            update_book_quantity(book_id, 1)
            save_loans(loans)
            print("✔️ Devolução registrada com sucesso!")
            break
