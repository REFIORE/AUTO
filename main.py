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


def main():
    if not os.path.exists("key.key"):
        write_key()
    key = load_key()
    fer = Fernet(key)
    add(fer)


if __name__ == '__main__':
    main()
