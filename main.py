from getpass import getpass
from crypto import encrypt_text

def main():
    while True:
        print("\n Text Encryptinator")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")

        user_choice = input("Choose an option: ")


        if user_choice == "1":
            text = input("Enter text to encrypt: ")
            # TODO: Figure out why getpass didn't work
            password = input("Enter password: ")

            if not password:
                print("Password cannot be empty.")
                continue

            encrypted = encrypt_text(text, password)
            print(f"\n Encrypted text: {encrypted}")
            continue

        # TODO: refer to decryptor
        if user_choice == "2":
            break

        if user_choice == "3":
            break

        if user_choice not in ("1", "2"):
            print("Invalid option.")
            continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
