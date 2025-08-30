import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fer = Fernet(key)


def write_key():
    with open("key.key", "wb") as f:
        f.write(key)


def load_key():
    with open("key.key", "r") as f:
        text = f.read(key)
        print(text)


def main():
    write_key()
    load_key()


if __name__ == '__main__':
    main()
