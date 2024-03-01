import hut
import amenity

tomy = hut.Hut("tommy", "Washington", "boop", 123, "poeflijgoi")
tomy.state = "Colorado"
print(tomy.state)
tomy.state = "vermont"
print(tomy.state)

tomy.elevation = 13466
print(tomy.elevation)

a = amenity.Amenity('hot tub', "a toasty tub to soak in")
a.description = 'boop'
print(a.description)