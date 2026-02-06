        #   "1": lambda: create_user,
        #     "2": lambda: list_users,

from models import User
import csv
import os

FILE_PATH_USERS = "Sistema_biblioteca\\data\\users.csv"

def load_users():
    users = []

    if not os.path.exists(FILE_PATH_USERS):
        return users
    
    with open(FILE_PATH_USERS, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            user = User(
                row["id"],
                row["name"],
                row["email"]
            )

            users.append(user)

        return users
    
def save_users(users):
    with open(FILE_PATH_USERS,"w", newline="", encoding="utf-8") as file:
        fieldnames = ["id","name","email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for user in users:
            writer.writerow({
               "id": user.id,
                "name": user.name,
                "email": user.email
            })

def get_next_user_id(users):
    if not users:
        return 1
    return max(user.id for user in users) + 1

def create_user():
    print("\n\nRegistrando usuário...\n")
    name = input("Nome: ")
    email = input("Email: ")
    users = load_users()
    user_id = get_next_user_id(users)

    new_user = User(user_id, name, email)
    users.append(new_user)
    save_users(users)
    print(f"\n ✔️ Usuário {name} registrado com sucesso com ID {user_id}")

def list_users():
    users = load_users()
    if not users:
        print("\nNenhum usuário cadastrado.")
        return
    
    print("\n\nLista de usuários cadastrados:\n")
    for user in users:
        print(user.display())
        
def get_user_by_id(user_id):
    users = load_users()
    for user in users:
        if user.id == user_id:
            return user
    return None

    