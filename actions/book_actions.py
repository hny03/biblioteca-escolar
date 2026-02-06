from models import Book 
import csv
import os

FILE_PATH_BOOKS = "Sistema_biblioteca\\data\\books.csv"

# self, code, title, author, year, quantity):
def load_books():
    books = []

    if not os.path.exists(FILE_PATH_BOOKS):
        return books
    
    with open(FILE_PATH_BOOKS, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            book = Book(
                row["code"],
                row["title"],
                row["author"],
                row["year"],
                row["quantity"]
            )

            book.code = int(row["code"])
            book.disponibility = row["disponibility"] == "True"
            books.append(book)

        return books
    
def save_books(books):
    with open(FILE_PATH_BOOKS,"w", newline="", encoding="utf-8") as file:
        fieldnames = ["code","title","author","year","disponibility","quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for book in books:
            writer.writerow({
               "code": book.code,
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "disponibility": book.disponibility,
                "quantity": book.quantity
            })

        

def get_next_book_code(books):
    if not books:
        return 1
    return max(book.code for book in books) + 1


def create_book():
    print("\n\nRegistrando livro...")
    title = input("\nTítulo: ")
    author = input("Autor: ")
    year = input("Ano: ")
    quantity = input("Quantidade: ")
    
    books = load_books()
    code = get_next_book_code(books)
    
    new_book = Book(code, title, author, year, quantity)
    books.append(new_book)
    save_books(books)

    print(f"\n ✔️ Livro '{title}' cadastrado com sucesso com o código {code}! ")

def update_book_quantity(code = None, quantity = None):

    books = load_books()
    
    if not books:
        print("Nenhum livro cadastrado")
        return
    
    if(code is None and quantity is None):
        print("\n\nAtualizar quantidade de um livro...\n")
        code = int(input("Código do livro:"))
        quantity = input("Quantidade removida/adicionada (use '-x' para remover): ")
    
    for book in books:
        if book.code == code:
            book.change_quantity(int(quantity))
            save_books(books)
            print(f"✔️ Quantidade do livro '{book.title}' atualizada para {book.quantity}")
            return

def list_books():
    
    print("\n\nListando livros...\n")
    books = load_books()

    if not books:
        print("🧐 Nenhum livro cadastrado")
        return
    
    for book in books:
        print(book.display())

def get_book_by_code(code):
    books = load_books()
    for book in books:
        if book.code == code:
            return book
    return None