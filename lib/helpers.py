# lib/helpers.py
from models.hut import Hut

def print_hut_data():
    huts = Hut.get_all()
    for hut in huts:
        print(hut)

def find_hut_by_name():
    name = input("Enter the hut's name: ")
    hut = Hut.find_by_name(name)
    print(hut) if hut else print(f'Hut {name} not found')

def exit_program():
    print("Goodbye!")
    exit()
