# lib/cli.py
from models.hut_amenity import HutAmenity
from models.amenity import Amenity

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
    print_hut_details,
    update_hut_details,
    print_hut_ameities,
    delete_amenity_from_hut,
    delete_hut,
    print_amenity_details,
    update_amenity_details,
    print_huts_with_chosen_amenity,
    delete_amenity,
    select_a_hut,
    select_amenity
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
                # individual hut menu
                elif hut_menu_choice == "2":
                    print_hut_data()
                    hut_found = select_a_hut()
                    if hut_found != None:
                        while True:
                            print("")
                            print(f'         ----- Edit {hut_found.name.title()} -----')
                            single_hut_menu()
                            single_hut_menu_choice = input("         > ")
                            if single_hut_menu_choice == "0":
                                break
                            elif single_hut_menu_choice == "1":
                                print_hut_details(hut_found)
                            elif single_hut_menu_choice == "2":
                                update_hut_details(hut_found)
                            elif single_hut_menu_choice == "3":
                                print_hut_ameities(hut_found)
                            elif single_hut_menu_choice == "4":
                                add_amenity_to_hut(hut_found)
                            elif single_hut_menu_choice == "5":
                                delete_amenity_from_hut(hut_found)
                            elif single_hut_menu_choice == "6":
                                delete_hut(hut_found)
                            elif single_hut_menu_choice == "7":
                                exit_program()
                            else:
                                print('Invalid menu choice. Try again!')
                elif hut_menu_choice == "3":
                    add_new_hut()
                elif hut_menu_choice == "4":
                    exit_program()
                else:
                    print('Invalid menu choice!')
        # amenity menu
        elif choice == "2":
            while True:
                amenity_menu()
                amenity_menu_choice = input("> ")
                if amenity_menu_choice == "0":
                    break
                elif amenity_menu_choice == "1":
                    print_amenities()
                # specific amenity menu
                elif amenity_menu_choice == "2":
                    print_amenities()
                    amenity_found = select_amenity()
                    if amenity_found != None:
                        while True:
                            print("")
                            print(f'         ----- Edit {amenity_found.name.title()} Amenity -----')
                            single_amenity_menu()
                            single_amenity_menu_choice = input("         > ")
                            if single_amenity_menu_choice == "0":
                                break
                            elif single_amenity_menu_choice == "1":
                                print_amenity_details(amenity_found)
                            elif single_amenity_menu_choice == "2":
                                update_amenity_details(amenity_found)
                            elif single_amenity_menu_choice == "3":
                                print_huts_with_chosen_amenity(amenity_found)
                            elif single_amenity_menu_choice == "4":
                                delete_amenity(amenity_found)
                            elif single_amenity_menu_choice == "5":
                                exit_program()
                            else:
                                print('Invalid menu choice. Try again!')
                elif amenity_menu_choice == "3":
                    create_new_amenity()
                elif amenity_menu_choice == "4":
                    exit_program()
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
    print("2. Select a hut")
    print("3. Create a new hut")
    print("4. Exit program")
    print("")

def single_hut_menu():
    print("         0. Exit Edit Hut")
    print("         1. Print hut details")
    print("         2. Update hut details")
    print("         3. View hut amenities")
    print("         4. Add an amenity to hut")
    print("         5. Remove amenity from hut")
    print("         6. Delete hut")
    print("         7. Exit program")
    print("")

def amenity_menu():
    print("")
    print("----- Amenity Menu -----")
    print("0. Exit Amenity Menu")
    print("1. View all amenity data")
    print("2. Select an amenity by name")
    print("3. Create a new amenity")
    print("4. Exit program")
    print("")

def single_amenity_menu():
    print("         0. Exit Edit Amenity")
    print("         1. Print amenity details")
    print("         2. Update amenity details")
    print("         3. View huts with this amenitiy")
    print("         4. Delete amenity")
    print("         5. Exit program")
    print("")

if __name__ == "__main__":
    main()
