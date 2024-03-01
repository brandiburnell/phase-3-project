from __init__ import CURSOR, CONN

class Amenity:
     
    # dictionary of all amenities
    amenities = {}

    def __init__(self, name, description, id=None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Amenity {self.id} {self.name}, {self.description}"
    
    ####################################
    # property definitions and setters #
    ####################################

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description):
            self._description = description
        else:
            raise ValueError("Description must be a non-empty string")
        
    ####################################
                # methods #
    ####################################
    
    @classmethod
    def create_table(cls):
        """ create a new table to persist attributes of Amenity instances """
        sql = """
            CREATE TABLE IF NOT EXISTS amenities (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Amenity instances """
        sql = """
            DROP TABLE IF EXISTS amenities
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with amenity info. Update object id attribute using
        primary key value of new row """
        sql = """
            INSERT INTO amenities (name, description)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.description))
        CONN.commit()

        self.id = CURSOR.lastrowid
    
    @classmethod
    def create(cls, name, description):
        """ Initialize a new Amenity instance and save object to db """
        amenity = cls(name,description)
        amenity.save()
        return amenity
    
    def update(self):
        """ Update the table row corresponding to the current Amenity instance"""
        sql = """
            UPDATE amenities
            SET name = ?, description = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.description))
        CONN.commit()
    
    def delete(self):
        """ Delete the table row corresponding to the current Amenity instance """
        sql = """
            DELETE FROM amenities
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id))
        CONN.commit()
    