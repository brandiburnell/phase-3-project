from models.__init__ import CONN, CURSOR
from models.amenity import Amenity
from models.hut import Hut
from models.hut_amenity import HutAmenity

Amenity.drop_table()
Amenity.create_table()
Hut.drop_table()
Hut.create_table()
HutAmenity.drop_table()
HutAmenity.create_table()

# Create Seed Data
def seed_database():
    hut1 = Hut.create("Fortune Peak Hut", "Washington", "Fortune Peak Huts", 3760, "https://www.fortunecreekhuts.com/huts")
    hut2 = Hut.create("Continental Divide Cabin","Colorado", "10th Mountain Division", 10512, "https://www.huts.org/The_Huts/continental_divide.php")
    hut3 = Hut.create("Norway Camp", "Oregon", "Wallowa Huts", 6895, "http://wallowahuts.com/norway.php")
    hut4 = Hut.create("Baldy Knoll Yurt", "Wyoming", "Teton Backcountry Guides", 8800, "https://tetonbackcountryguides.com/meet-our-yurts/baldy-knoll/")
    hut5 = Hut.create("St Paul Hut", "Colorado", "Private", 11440, "https://stpaulhut.com/")

    hot_tub = Amenity.create("Hot Tub", "A warm, communal bath")
    stove = Amenity.create("Stove", "A propane stovetop used to prepare meals")
    sleeping_pads = Amenity.create("Sleeping Pads", "Some form of pad or mattress visitors can use to sleep on")
    water_filter = Amenity.create("Water filter", "A water purification device for snowmelt")
    lighting = Amenity.create("Lighting", "Solar powered overhead lighting is available")
    firewood = Amenity.create("Firewood", "Firewood is provided to be used in the wood stove for heating")


    HutAmenity.create(hut1.id, hot_tub.id)
    HutAmenity.create(hut1.id, sleeping_pads.id)
    HutAmenity.create(hut1.id, lighting.id)
    HutAmenity.create(hut1.id, stove.id)

    HutAmenity.create(hut2.id, firewood.id)
    HutAmenity.create(hut2.id, sleeping_pads.id)
    HutAmenity.create(hut2.id, lighting.id)

    HutAmenity.create(hut3.id, firewood.id)
    HutAmenity.create(hut3.id, sleeping_pads.id)

    HutAmenity.create(hut4.id, hot_tub.id)
    HutAmenity.create(hut4.id, stove.id)
    HutAmenity.create(hut4.id, sleeping_pads.id)
    HutAmenity.create(hut4.id, water_filter.id)
    HutAmenity.create(hut4.id, lighting.id)
    HutAmenity.create(hut4.id, firewood.id)

    HutAmenity.create(hut5.id, water_filter.id)

seed_database()
print("Seeded Database")