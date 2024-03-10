# lib/helpers.py
from models.__init__ import CURSOR, CONN
from models.hut import Hut
from models.amenity import Amenity
from models.hut_amenity import HutAmenity

def print_hut_data():
    huts = Hut.get_all()
    for hut in huts:
        print(hut)

def find_hut_by_name():
    name = input("Enter the hut's name: ")
    hut = Hut.find_by_name(name)
    if hut:
        return hut
    else:
        print("")
        print(f'     Uh oh! Hut "{name}" not found :( ')
        print("")
        print('Please select an option below: ')
        return None

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
        print(f'             Amenity name: {amenity.name}')
        print(f'             Amenity descripton: {amenity.description}')
        print("")

def find_amenity_by_name():
    name = input("Enter the name of the amenity: ")
    amenity = Amenity.find_by_name(name)
    print(amenity) if amenity else print(f'Amenity {name} not found')

def create_new_amenity():
    print("         Enter the new amenity's details below:")
    name = input("         Name of amenity: ")
    description = input("         Description of amenity: ")
    try:
        new_amenity = Amenity.create(name, description)
        print(f'         Success: {new_amenity.name}, {new_amenity.description}')
        return new_amenity
    except Exception as exc:
        print('        Error creating amenity: ', exc)

def delete_amenity():
    name = input("Enter the name of the amenity you would like to delete: ")
    amenity = Amenity.find_by_name(name)
    if amenity:
        amenity.delete()
        print(f'Amenity {name} has been deleted')
    else:
        print(f'Amenity {name} not found')

def add_amenity_to_hut(hut):
    print('function')
    # update hut_amerity table with passe dhut id and new amenity id
    # amenity_name = input("Please enter the name of the amenity: ")
    # hut_amenity = Hut.add_amenity()

def exit_program():
    print("Goodbye!")
    exit()

def print_hut_details(hut):
    print(f'             Hut name: {hut.name}')
    print(f'             Hut state: {hut.state}')
    print(f'             Hut system: {hut.system}')
    print(f'             Hut elevation: {hut.elevation}')
    print(f'             Hut website address: {hut.url}')

def update_hut_details(hut):
    print("        Please enter the hut details you would like to update below.")
    print("        If you would not like to change the hut attribute, press enter to move onto the next option.")
    name = input("        Please enter the new hut name: ")
    state = input("        Please enter the new state: ")
    system = input("        Please enter the new hut system: ")    
    elevation = input("        Please enter the new elevation: ")
    url = input("        Please enter the new website address: ")
    if name != "":
        hut.name = name
    if state != "":
        hut.state = state
    if system != "":
        hut.system = system
    if elevation!= "":
        hut.elevation = int(elevation)
    if url != "":
        hut.url = url

    hut.update()
    print("")
    print(f'         Hut "{hut.name}" has been successfully updated!')

def print_hut_ameities(hut):
    # query hut_amenities for rows that match the given hut id
    sql = """
        SELECT amenity_id
        FROM hut_amenities
        WHERE hut_id = ? 
        """
    rows = CURSOR.execute(sql, (hut.id,)).fetchall()
    if len(rows):
        for row in rows:
            amenity = Amenity.find_by_id(row[0])
            print(f'         {amenity.name}: {amenity.description}')
    else:
        print("")
        print('         No amenities found. Sounds like camping!')


