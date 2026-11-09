import binascii

from getpass import getpass
from crypto import encrypt_text, decrypt_text
from cryptography.exceptions import InvalidTag

def main():
    while True:
        print("\n Text Encryptinator")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")

        user_choice = input("Choose an option: ")


        if user_choice == "1":
            text = input("Enter text to encrypt: ")
            # TODO 1: Figure out why getpass didn't work
            password = input("Enter password: ")

            if not password:
                print("Password cannot be empty.")
                continue

            encrypted = encrypt_text(text, password)
            print(f"\n Encrypted text: {encrypted}")
            continue

        if user_choice == "2":
            text = input("Enter text to decrypt: ")
            # TODO: Implement getpass if TODO 1 is done
            password = input("Enter password: ")

            try:
                decrypted = decrypt_text(text, password)
                print(f"\nDecrypted text: {decrypted}")
            except (InvalidTag, ValueError, binascii.Error):
                print("Invalid password or encrypted data,")

            continue

        if user_choice == "3":
            break

        if user_choice not in ("1", "2"):
            print("Invalid option.")
            continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
