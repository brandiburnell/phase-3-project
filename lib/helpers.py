# lib/helpers.py
from models.__init__ import CURSOR, CONN
from models.hut import Hut
from models.amenity import Amenity
from models.hut_amenity import HutAmenity

def print_hut_data():
    huts = Hut.get_all()
    for index, hut in enumerate(huts):
        print(f'{index+1} •{hut.name.title()}, {hut.system.title()}, {hut.state}.')
        print("  Elevation: {:,}".format(hut.elevation) + f' ft, Website: {hut.url}•')
        print("")

def select_a_hut():
    num_selected = int(input("Enter the number corresponding to the hut you would like to select: "))
    huts = Hut.get_all()
    try: 
        hut_selected = huts[num_selected - 1]
        return hut_selected
    except Exception as exc:
        print("")
        print(f'     Uh oh! Hut "{num_selected}" not found :( ')
        print("")
        print('Please select an option below: ')
        return None

def find_hut_by_name():
    name = input("Enter the hut's name: ").lower()
    hut = Hut.find_by_name(name)
    if hut:
        return hut
    else:
        print("")
        print(f'     Uh oh! Hut "{name.title()}" not found :( ')
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
        print(f'Success: {new_hut.name.title()} has been created!')
    except Exception as exc:
        print('Error creating hut: ', exc)

def delete_hut():
    name = input("Enter the name of the hut: ")
    hut = Hut.find_by_name(name)
    if hut:
        hut.delete()
        print(f'Hut {name.title()} deleted')
    else:
        print(f'Hut {name.title()} not found')

def print_amenities():
    amenities = Amenity.get_all()
    for amenity in amenities:
        print(f'             Amenity name: {amenity.name.title()}')
        print(f'             Amenity descripton: {amenity.description}')
        print("")

def find_amenity_by_name():
    name = input("Enter the name of the amenity: ")
    amenity = Amenity.find_by_name(name)
    
    if amenity:
        return amenity
    else:
        print("")
        print(f'     Uh oh! Amenity "{name.title()}" not found :( ')
        print("")
        print('Please select an option below: ')
        return None

def create_new_amenity():
    print("         Enter the new amenity's details below:")
    name = input("         Name of amenity: ")
    description = input("         Description of amenity: ")
    try:
        new_amenity = Amenity.create(name, description)
        print(f'         Success: {new_amenity.name.title()}, {new_amenity.description}')
        return new_amenity
    except Exception as exc:
        print('         Error creating amenity: ', exc)

def delete_amenity():
    name = input("Enter the name of the amenity you would like to delete: ")
    amenity = Amenity.find_by_name(name)
    if amenity:
        amenity.delete()
        print(f'Amenity {name.title()} has been deleted')
        
    else:
        print(f'Amenity {name.title()} not found')

def add_amenity_to_hut(hut):
    print('         Enter "existing" if you would like to add an existing amenity to the hut.')
    print('         Enter "new" if you would like to add a new amenity to the hut.')
    new_or_existing = input("         > ").lower()
    if new_or_existing == "existing":
        print("         Please choose an amenity to add from the list below: ")
        print_amenities()
        amenity_chosen = input("        Enter the name of the amenity you would like to add to the hut: ")
        amenity = Amenity.find_by_name(amenity_chosen)
        try:
            HutAmenity.create(hut.id, amenity.id)
            print("")
            print(f'            {amenity.name.title()} has been added to {hut.name.title()}')
        except Exception as exc:
            print("")
            print(f'             Amenity "{amenity_chosen}" not found')
    elif new_or_existing == "new":
        amenity = create_new_amenity()
        try:
            HutAmenity.create(hut.id, amenity.id)
            print("")
            print(f'            {amenity.name.title()} has been added to {hut.name.title()}')
        except Exception as exc:
            print("")
            print('             Error adding amenity: ', exc)
    else:
        print("")
        print("             Invalid choice")

def delete_amenity_from_hut(hut):
    amenity_name = input('         Enter the name of the amenity you woule like to delete from the hut: ')
    try:
        amenity = Amenity.find_by_name(amenity_name)
        sql = """
            DELETE 
            FROM hut_amenities
            WHERE hut_id = ? 
                AND amenity_id = ?
        """
        CURSOR.execute(sql, (hut.id, amenity.id))
        CONN.commit()

        print("")
        print(f'            {amenity.name.title()} has been removed from {hut.name.title()}')
    except Exception as exc:
        print(f'            "{amenity_name}" not found. Please try again')

def exit_program():
    print("Goodbye!")
    exit()

def print_hut_details(hut):
    print(f'             Hut name: {hut.name.title()}')
    print(f'             Hut state: {hut.state}')
    print(f'             Hut system: {hut.system.title()}')
    print("             Hut Elevation: {:,}".format(hut.elevation))
    print(f'             Hut website address: {hut.url}')

def update_hut_details(hut):
    print("        Please enter the hut details you would like to update below.")
    print("        If you would not like to change the hut attribute, press enter to move onto the next option.")
    name = input("        Please enter the new hut name: ")
    state = input("        Please enter the new state: ")
    system = input("        Please enter the new hut system: ")    
    elevation = input("        Please enter the new elevation: ")
    url = input("        Please enter the new website address: ")
    print("")
    error_counter = 0
    if name != "":
        try:
            hut.name = name
        except Exception as exc:
            print('        Error updating hut name: ', exc)
            error_counter += 1
    if state != "":
        try:
            hut.state = state
        except Exception as exc:
            print('        Error updating hut state: ', exc)
            error_counter += 1
    if system != "":
        try:
            hut.system = system
        except Exception as exc:
            print('        Error updating hut system: ', exc)
            error_counter += 1
    if elevation!= "":
        try:
            hut.elevation = int(elevation)
        except Exception as exc:
            print('        Error updating hut elevation: ', exc)
            error_counter += 1
    if url != "":
        try:
            hut.url = url
        except Exception as exc:
            print('        Error updating hut url: ', exc)
            error_counter += 1

    hut.update()
    if error_counter == 0:
        print(f'         Hut "{hut.name.title()}" has been successfully updated!')

def print_hut_ameities(hut):
    # query hut_amenities for rows that match the given hut id
    sql = """
        SELECT amenity_id
        FROM hut_amenities
        WHERE hut_id = ? 
        """
    rows = CURSOR.execute(sql, (hut.id,)).fetchall()
    if len(rows):
        print("")
        for row in rows:
            amenity = Amenity.find_by_id(row[0])
            print(f'             {amenity.name.title()}: {amenity.description}')
    else:
        print("")
        print('             No amenities found. Sounds like camping!')

def delete_hut(hut):
    sql = """
    DELETE
    FROM hut_amenities
    WHERE hut_id = ?
    """
    CURSOR.execute(sql, (hut.id,))
    hut.delete()
    print(f'         {hut.name.title()} has been deleted')

def print_amenity_details(amenity):
    print(f'             Amenity name: {amenity.name.title()}')
    print(f'             Amenity description: {amenity.description}')

def update_amenity_details(amenity):
    print("        Please enter the amenity details you would like to update below.")
    print("        If you would not like to change the amenity attribute, press enter to move onto the next option.")
    name = input("        Please enter the new amenity name: ")
    description = input("        Please enter the new description: ")
    print("")
    error_counter = 0
    if name != "":
        try:
            amenity.name = name
        except Exception as exc:
            print('        Error updating amenity name: ', exc)
            error_counter += 1
    if description != "":
        try:
            amenity.description = description
        except Exception as exc:
            print('        Error updating amenity description: ', exc)
            error_counter += 1
    amenity.update()
    if error_counter == 0:
        print(f'         Amenity "{amenity.name.title()}" has been successfully updated!')

def print_huts_with_chosen_amenity(amenity):
    # query hut_amenities for rows that match the given amenity id
    sql = """
        SELECT hut_id
        FROM hut_amenities
        WHERE amenity_id = ? 
        """
    rows = CURSOR.execute(sql, (amenity.id,)).fetchall()
    if len(rows):
        print("")
        for row in rows:
            hut = Hut.find_by_id(row[0])
            print(f'             {hut.name.title()}: {hut.state}, {hut.system.title()}')
    else:
        print("")
        print('             No huts with this amenity found. Keep dreaming!')

def delete_amenity(amenity):
    sql = """
    DELETE
    FROM hut_amenities
    WHERE amenity_id = ?
    """
    CURSOR.execute(sql, (amenity.id,))
    amenity.delete()
    print(f'         {amenity.name.title()} has been deleted')