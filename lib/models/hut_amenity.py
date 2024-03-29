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
            CREATE TABLE IF NOT EXISTS hut_amenities (
            id INTEGER PRIMARY KEY,
            hut_id INTEGER,
            amenity_id INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Hut instances """
        sql = """
            DROP TABLE IF EXISTS hut_amenities;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """ Inser a new row with hut amenity information. Update id attribute using
        primary key value of new row """
        sql = """
            INSERT INTO hut_amenities (hut_id, amenity_id)
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
        sql = """
            UPDATE hut_amenities
            SET hut_id = ?, amenity_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.hut_id, self.amenity_id, self.id))
        CONN.commit()
    
    def delete(self):
        """ Delete table row corresponding to current HutAmenity instance """
        sql = """
            DELETE FROM hut_amenities
            WHERE id = ? 
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a HutAmenity object having the values from this table row """
        hut_amenity = cls.all.get(row[0])
        if hut_amenity:
            hut_amenity.hut_id = row[1]
            hut_amenity.amenity_id = row[2]
        else:
            hut_amenity = cls(row[1], row[2])
            hut_amenity.id = row[0]
            cls.all[hut_amenity.id] = hut_amenity
        return hut_amenity

    @classmethod
    def get_all(cls):
        """ Return a list containg a HutAmenity object for each row in hut-amenities """
        sql = """
            SELECT *
            FROM hut_amenities 
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
     
    @classmethod
    def find_by_hut_and_amenity(cls, hut_id, amenity_id):
        """ Return a hut_amenity instance with a specific hut and amenity"""
        sql = """
            SELECT *
            FROM hut_amenities
            WHERE hut_id = ?
                AND amenity_id = ?
        """
        row = CURSOR.execute(sql, (hut_id, amenity_id)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def delete_hut(cls, hut_id):
        sql = """
            DELETE
            FROM hut_amenities
            WHERE hut_id = ?
        """
        CURSOR.execute(sql, (hut_id,))
        CONN.commit()
        
        for key, value in cls.all.items():
            if key == "hut_id" and value == hut_id:
                del cls.all.items[key]

    @classmethod
    def delete_amenity(cls, amenity_id):
        sql = """
            DELETE
            FROM hut_amenities
            WHERE amenity_id = ?
        """
        CURSOR.execute(sql, (amenity_id,))
        CONN.commit()
        
        for key, value in cls.all.items():
            if key == "amenity_id" and value == amenity_id:
                del cls.all.items[key]


