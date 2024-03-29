from models.__init__ import CURSOR, CONN

class Hut:

    # dictionary of all huts saved to db
    all = {}

    # list of all states
    state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", 
                   "Arizona", "California", "Colorado", "Connecticut", "District ", 
                   "of Columbia", "DelawSare", "Florida", "Georgia", "Guam", "Hawaii", 
                   "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", 
                   "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", 
                   "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", 
                   "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", 
                   "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", 
                   "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", 
                   "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", 
                   "Washington", "Wisconsin", "West Virginia", "Wyoming"]


    def __init__(self, name, state, system, elevation, url, id=None):
        self.id = id
        self.name = name
        self.state = state
        self.system = system
        self.elevation = elevation
        self.url = url

    def __repr__(self):
        return f"<Hut {self.id}: {self.name}, {self.state}, {self.system}, {self.elevation}, {self.url}>"

    ####################################
    # property definitions and setters #
    ####################################

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name.lower()
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        if isinstance(state, str) and len(state) and (state.capitalize() in Hut.state_names):
            self._state = state.capitalize()
        else: 
            raise ValueError("State must be a non-empty string and one of the 50 states")
        
    @property
    def system(self):
        return self._system
    
    @system.setter
    def system(self, system):
        if isinstance(system, str) and len(system):
            self._system = system.lower()
        else:
            raise ValueError("System must be a non-empty string")
        
    @property
    def elevation(self):
        return self._elevation
    
    @elevation.setter
    def elevation(self, elevation):
        if isinstance(elevation, int) and (0 < elevation < 14000):
            self._elevation = elevation
        else:
            raise ValueError("Elevation must be an integer greater than 0 and less than 14,000")
    
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, url):
        if isinstance(url, str) and len(url):
            self._url = url
        else:
            raise ValueError("Hut website URL must be a non-empty string")
        
    ####################################
                # methods #
    ####################################
    
    @classmethod
    def create_table(cls):
        """ Create new table to persist attributes of Hut instances """
        sql = """
            CREATE TABLE IF NOT EXISTS huts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            state TEXT,
            system TEXT,
            elevation INTEGER,
            url TEXT)
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Hut instances """
        sql = """
            DROP TABLE IF EXISTS huts;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """ Insert a new row with hut attributes 
        Update object id attribute using primary key value of new row
        Save object in local dictionary using PK as dictionary key
        """
        sql = """
            INSERT INTO huts (name, state, system, elevation, url)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.state, self.system, self.elevation, self.url))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        """ Update table row corresponding to current Hut instance """
        sql = """
            UPDATE huts
            SET name = ?, state = ?, system = ?, elevation = ?, url = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.state, self.system,
                             self.elevation, self.url, self.id))
        CONN.commit()
    
    def delete(self):
        """ Delete table row correspoding to current Hut instance """
        sql = """
            DELETE FROM huts
            WHERE name = ?
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        
        # why do you need to do type(self) first
        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def create(cls, name, state, system, elevation, url):
        """ Initialize new instance to save the object to db """
        hut = cls(name, state, system, elevation, url)
        hut.save()
        return hut
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return employee object having attribute values from row """
        hut = cls.all.get(row[0])
        if hut:
            hut.name = row[1]
            hut.state = row[2]
            hut.system = row[3]
            hut.elevation = row[4]
            hut.url = row[5]
        else:
            hut = cls(row[1], row[2], row[3], row[4], row[5])
            hut.id = row[0]
            cls.all[hut.id] = hut
        return hut

    @classmethod
    def get_all(cls):
        """ Return a list containing a Hut object per row in the table """
        sql = """
            SELECT *
            FROM huts
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        """ Return hut with the matching name """
        sql = """
            SELECT *
            FROM huts
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name.lower(),)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        """ Return hut with the matching name """
        sql = """
            SELECT *
            FROM huts
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def get_hut_amenities(self):
        from models.amenity import Amenity
        # query hut_amenities for rows that match the given hut id
        sql = """
            SELECT amenity_id
            FROM hut_amenities
            WHERE hut_id = ? 
            """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        if len(rows):
            amenities = set()
            for row in rows:
                amenity = Amenity.find_by_id(row[0])
                amenities.add(amenity)
            return amenities
        else:
            return None


    

        
    



