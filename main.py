import os.path
from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)


def load_key():
    with open("key.key", "rb") as text:
        password = text.read()
    return password


def add(fer):
    login = input("Введите логин:")
    password = input("Введите пароль:")
    with open("passwords.txt", "w") as file:
        encrypted_password = fer.encrypt(password.encode()).decode()
        file.write(f"{login}|{encrypted_password}\n")


def view(fer):
    with open("passwords.txt", "r") as text:
        for line in text:
            login, password = line.split('|')
            decrypted_password = fer.decrypt(password.encode()).decode()
            print(f"Логин: {login} | Пароль: {decrypted_password}")


def action_selection(fer):
    status = False
    while not status:
        choice = input("Хотите добавить новый пароль или посмотреть уже существующие \n1. Посмотреть, \n2. Добавить? \n3. Выйти\n")
        choice = int(choice)
        if choice == 1:
            view(fer)
        elif choice == 2:
            add(fer)
        else:
            status = True


def main():
    if not os.path.exists("key.key"):
        write_key()
    key = load_key()
    fer = Fernet(key)
    action_selection(fer)


if __name__ == '__main__':
    main()
