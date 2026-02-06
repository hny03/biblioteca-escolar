class Book:
    def __init__(self, code, title, author, year, quantity):
        self.code = code
        self.title = title
        self.author = author
        self.year = int(year)
        # normalize quantity to int before using it
        self.quantity = int(quantity)
        self.disponibility = True if self.quantity > 0 else False

    def __repr__(self):
        return f'book({self.code}, {self.title}, {self.author}, {self.year}, {self.disponibility}, {self.quantity})'

    def change_quantity(self, number):
        self.quantity = self.quantity + number

        if self.quantity <= 0:
            self.disponibility = False
        
        elif self.quantity > 0 and self.disponibility == False:
            self.disponibility = True

    def display(self):
        return f'Código: {self.code} | Título: {self.title} | Autor: {self.author} | Ano: {self.year} | Disponibilidade: {"Disponível" if self.disponibility else "Indisponível"} | Quantidade: {self.quantity}'






class User:
    def __init__(self, id, name, email):
        self.id = int(id)
        self.name = name
        self.email = email

    def __repr__(self):
        return f'user({self.id}, {self.name}, {self.email})'
    
    def display(self):
        return f'ID: {self.id} | Nome: {self.name} | Email: {self.email}'
    




class Loan:
    def __init__(self, id, book, user, loan_date, return_date, status):
        self.id = int(id)
        self.book = book
        self.user = user
        self.loan_date = loan_date
        self.return_date = return_date
        self.status = status
        
    def change_status(self, new_status):
        self.status = new_status