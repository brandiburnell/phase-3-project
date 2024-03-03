# lib/cli.py

from helpers import (
    exit_program,
    print_hut_data,
    find_hut_by_name
)


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            while True:
                hut_menu()
                hut_menu_choice = input("> ")
                if hut_menu_choice == "0":
                    break
                elif hut_menu_choice == "1":
                    print_hut_data()
                elif hut_menu_choice == "2":
                    find_hut_by_name()
        elif choice == "2":
            find_hut_by_name()
        else:
            print("Invalid choice")


def main_menu():
    print("")
    print("************ MAIN MENU ************")
    print("")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Hut menu")
    print("")
    print("***********************************")
    print("")


def hut_menu():
    print("")
    print("----- Hut Menu -----")
    print("1. View all hut data")
    print("2. Find a hut by name")
    print("")



if __name__ == "__main__":
    main()
