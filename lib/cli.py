# lib/cli.py

from helpers import (
    exit_program,
    print_hut_data,
    find_hut_by_name,
    add_new_hut,
    delete_hut,
    print_amenities,
    find_amenity_by_name,
    create_new_amenity,
    delete_amenity,
    add_amenity_to_hut,
    print_hut_details
)


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        # hut menu
        elif choice == "1":
            while True:
                hut_menu()
                hut_menu_choice = input("> ")
                if hut_menu_choice == "0":
                    break
                elif hut_menu_choice == "1":
                    print_hut_data()
                elif hut_menu_choice == "2":
                    hut_found = find_hut_by_name()
                    if hut_found != None:
                        while True:
                            single_hut_menu()
                            single_hut_menu_choice = input("> ")
                            if single_hut_menu_choice == "0":
                                break
                            if single_hut_menu_choice == "1":
                                print_hut_details(hut_found)
                            


                    # hut_name = input("get name")
                    # hut = find_hut_by_name(name)
                    # while:
                    #     another function(hut)
                elif hut_menu_choice == "3":
                    add_new_hut()
                elif hut_menu_choice == "4":
                    delete_hut()
                elif hut_menu_choice == "5":
                    add_amenity_to_hut()
                else:
                    print('Invalid menu choice!')
        elif choice == "2":
            while True:
                amenity_menu()
                amenity_menu_choice = input("> ")
                if amenity_menu_choice == "0":
                    break
                elif amenity_menu_choice == "1":
                    print_amenities()
                elif amenity_menu_choice == "2":
                    find_amenity_by_name()
                elif amenity_menu_choice == "3":
                    create_new_amenity()
                elif amenity_menu_choice == "4":
                    delete_amenity()
                else:
                    print('Invalid menu choice!')
        else:
            print("Invalid choice!")    


def main_menu():
    print("")
    print("************ MAIN MENU ************")
    print("")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Hut menu")
    print("2. Amenity Menu")
    print("")
    print("***********************************")
    print("")


def hut_menu():
    print("")
    print("----- Hut Menu -----")
    print("0. Exit Hut Menu")
    print("1. View all hut data")
    print("2. Select a hut by name")
    print("3. Create a new hut")
    print("4. Delete a hut") # maybe delete this one
    print("5. Add an amenity to a hut")
    print("")

def single_hut_menu():
    print("")
    print("         ----- Edit Hut -----")
    print("         0. Exit Edit Hut")
    print("         1. Print hut details")
    print("         2. Update hut details")
    print("         3. Add an amenity to hut")
    print("         4. Delete hut")

def amenity_menu():
    print("")
    print("----- Amenity Menu -----")
    print("0. Exit Amenity Menu")
    print("1. View all amenity data")
    print("2. Find an amenity by name")
    print("3. Create a new amenity")
    print("4. Delete an amenity")
    print("")


if __name__ == "__main__":
    main()
