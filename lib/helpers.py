# lib/helpers.py
from models.hut import Hut
from models.amenity import Amenity

def print_hut_data():
    huts = Hut.get_all()
    for hut in huts:
        print(hut)

def find_hut_by_name():
    name = input("Enter the hut's name: ")
    hut = Hut.find_by_name(name)
    print(hut) if hut else print(f'Hut {name} not found')

def add_new_hut():
    print("Enter the new hut's details below:")
    name = input("Hut name: ")
    state = input("The state the hut is located in: ")
    system = input("Hut system: ")
    elevation = input("Hut elevation: ")
    url = input("Hut website url: ")
    try:
        new_hut = Hut.create(name, state, system, int(elevation), url)
        print(f'Success: {new_hut}')
    except Exception as exc:
        print('Error creating hut: ', exc)

def delete_hut():
    name = input("Enter the name of the hut: ")
    hut = Hut.find_by_name(name)
    if hut:
        hut.delete()
        print(f'Hut {name} deleted')
    else:
        print(f'Hut {name} not found')

def print_amenities():
    amenities = Amenity.get_all()
    for amenity in amenities:
        print(amenity)

def find_amenity_by_name():
    name = input("Enter the name of the amenity: ")
    amenity = Amenity.find_by_name(name)
    print(amenity) if amenity else print(f'Amenity {name} not found')

def create_new_amenity():
    print("Enter the new amenity's details below:")
    name = input("Name of amenity: ")
    description = input("Description of amenity: ")
    try:
        new_amenity = Amenity.create(name, description)
        print(f'Success: {new_amenity}')
    except Exception as exc:
        print('Error creating amenity: ', exc)

def delete_amenity():
    name = input("Enter the name of the amenity you would like to delete: ")
    amenity = Amenity.find_by_name(name)
    if amenity:
        amenity.delete()
        print(f'Amenity {name} has been deleted')
    else:
        print(f'Amenity {name} not found')

def exit_program():
    print("Goodbye!")
    exit()
