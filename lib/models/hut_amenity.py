from models.__init__ import CURSOR, CONN

class HutAmenity:

    # store all instances of HutAmenity 
    all = {}

    def __init__(self, hut_id, amenity_id, id=None):
        self.id = id
        self.hut_id = hut_id
        self.amenity_id = amenity_id
    
    def __repr__(self):
        return f"<HutAmenity {self.id}, Hut ID: {self.hut_id}, Amenity ID: {self.amenity_id}"
    
    ####################################
    # property definitions and setters #
    ####################################

    @property
    def hut_id(self):
        return self._hut_id
    
    # might want to figure out some way of making sure hut id is part of actual existing IDs
    @hut_id.setter
    def hut_id(self, hut_id):
        if isinstance(hut_id, int):
            self._hut_id = hut_id
        else:
            raise ValueError("Hut ID must be an integer")
    
    @property
    def amenity_id(self):
        return self._amenity_id

    # might want to figure out some way of making sure amenity id is part of actual existing IDs
    @amenity_id.setter
    def amenity_id(self, amenity_id):
        if isinstance(amenity_id, int):
            self._amenity_id = amenity_id
        else:
            raise ValueError('Amenity ID must be an integer')
    
    ####################################
                # methods #
    ####################################
    
    @classmethod
    def create_table(cls):
        """ create a new table to persist arrtibutes of HutAmenity instances """
        sql = """
            CREATE TABLE IF NOT EXISTS hut-amenities
        """
        CURSOR.execute()
        CONN.commit()
    
    @classmethod
    def save(self):
        """ Inser a new row with hut amenity information. Update id attribute using
        primary key value of new row """
        sql = """
            INSERT INTO hut-amenities (hut-id, amenity-id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.hut_id, self.amenity_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, hut_id, amenity_id):
        """ Initialize a new hut amenity instance and save object to db """
        hut_amenity = cls(hut_id, amenity_id)
        hut_amenity.save()
        return hut_amenity

    def update(self):
        """ Update the table row corresponding to the current Hut Amenity instance """

