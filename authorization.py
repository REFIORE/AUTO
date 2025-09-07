from main import load_key
from main import Fernet


def authorization(fer, user_login, user_password):
    with open("passwords.txt", "r") as text:
        for line in text:
            login, password = line.split('|')
            decrypted_password = fer.decrypt(password.encode()).decode()
            if user_login == login and user_password == decrypted_password:
                print("Вы авторизованы")
                return True
            else:
                print("Такого пользователя не существует")


def main():
    key = load_key()
    fer = Fernet(key)
    status = False
    while not status:
        user_login = input("Логин: ")
        user_password = input("Пароль: ")
        if authorization(fer, user_login, user_password):
            break


if __name__ == '__main__':
    main()
