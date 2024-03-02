from __init__ import CURSOR, CONN

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
        pass

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
            self._system = system
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
            id INTEGER PRIMARY KEY
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
                             self.elevation, self.url))
    
    
        
    



