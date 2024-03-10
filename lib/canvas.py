from models.hut import Hut
from models.amenity import Amenity
from models.hut_amenity import HutAmenity

tomy = Hut("tommy", "Washington", "boop", 123, "poeflijgoi")
tomy.state = "Colorado"
print(tomy.state)
tomy.state = "vermont"
print(tomy.state)

tomy.elevation = 13466
print(tomy.elevation)

a = Amenity('hot tub', "a toasty tub to soak in")
a.description = 'boop'
print(a.description)

h = HutAmenity(1, 2)
print(h.hut_id)



