# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():
    while True:
        print("\n Text Encryptinator")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")

        user_choice = input("Choose an option: ")

        # TODO: refer to encryptor
        if user_choice == "1":
            break

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
