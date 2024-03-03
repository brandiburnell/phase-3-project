from models.__init__ import CURSOR, CONN

class HutAmenities:

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

    @amenity_id.setter
    def amenity_id(self, amenity_id):
        if isinstance(amenity_id, int):
            self._amenity_id = amenity_id
        else:
            raise ValueError('Amenity ID must be an integer')
    
    