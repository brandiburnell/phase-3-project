# Hut Hacker - A Backcountry Hut CLI
Backcountry huts provide unique and immersive expereinces for adventurers of all kinds. Nestled amidst stunning landscapes, these remote cabins offer refuge and shelter for hikers, skiers, and outdoor enthusiasts seeking to escape the hustle and bustle of city life. Whether tucked away in the snowy mountains or hidden within dense forests, staying at a backcountry hut offers a chance to disconnect from technology and reconnect with nature. 

Often, these huts are run by non-profit organizations and volunteers. It can be difficult to decipher exactly what amenities each hut has, as websites can be outdated and there is not a central repository for this information. Hut Hacker aims to store this information to help its user best plan for coming trips and excursions.

## Walkthrough

## Functions
The user has the ability to perform all CRUD actions. Specifically, the user can:
    - Create a new hut
    - Update an existing hut
    - Delete an existing hut
    - Print the details of an existing hut
    - Print all hut data
    - Add an amenity to a hut
    - Delete an amenity from a hut
    - Print all amenities that belongs to a hut
    - Create a new amenity
    - Update an existing amenity
    - Delete an amenity
    - Print all amenity data
    - Find all huts with a certain amenity

## Structure
This CLI app is organized into several python files. Their function and use is described below.
### cli.py
The menu logic and CLI functionality is contained in this file. Run this file to run the CLI. 
### amenity.py
This file contains the Amenity class. The Amenity class describes the amenities that a hut may possess. The Amenity class has two properties, name and description. The name of the amenity idetifies what it is, and the description helps provide additional detail.
### hut.py
hut.py contains the Hut class. The hut class models a backcountry hut and contains properties name, system, state, elevation, and url. These five properties provide the user with pertinent information about each hut.
### hut_amenity.py
The hut_amenity.py file contains the class for the joiner table between the Hut and Amenity classes. Hut and Amenity have a many-to-many relationship. This intermediary class keeps track of which huts have which amenities, and which amenities belong to each hut. The Hut_amenity class only has two properties, hut_id and amenity_id.

## Installation
Fork the repository and clone a copy onto your local machine. Prior to proceeding, ensure that Python 3 and pip are installed. Install necessary dependencies by executing 'pipenv install', then activate the virtual environment by running 'pipenv shell'.
### Seed Database
Run the following commands to seed the database:
```
python seed.py
```
### Run CLI
```
cd lib
python cli.py
```

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
