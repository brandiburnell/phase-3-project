from models.__init__ import CURSOR, CONN

class Amenity:
     
    # dictionary of all amenities
    amenities = {}

    def __init__(self, name, description, id=None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Amenity {self.id} {self.name}, {self.description}>"
    
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
        #### ask tommy about this line of code ####
        type(self).amenities[self.id] = self
    
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
            WHERE name = ?
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        del type(self).amenities[self.id]
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a Amenity object having the values from the table row """
        amenity = cls.amenities.get(row[0])
        if amenity:
            amenity.name = row[1]
            amenity.description = row[2]
        else:
            amenity = cls(row[1], row[2])
            amenity.id = row[0]
            cls.amenities[amenity.id] = amenity
        return amenity
    
    # get all
    @classmethod
    def get_all(cls):
        """ Return a list containing a Amenity object per row in amenities """
        sql = """
            SELECT *
            FROM amenities
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
        
    # find by id
    @classmethod
    def find_by_id(cls, id):
        """ Return an amenity corresponding to the given id """
        sql = """
            SELECT * 
            FROM amenities 
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    # other optional methods
    @classmethod
    def find_by_name(cls, name):
        """ Return an amenity corresponding to the given id """
        sql = """
            SELECT *
            FROM amenities
            WHERE name = ? 
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def huts(self):
        """ Return list of huts associated with each amenity """
        from models.hut import Hut
        sql = """
            SELECT * FROM amenities
            WHERE amenity_id"""