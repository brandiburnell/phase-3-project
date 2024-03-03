#!/usr/bin/env python3
# lib/debug.py

# from models.__init__ import CONN, CURSOR
from models.__init__ import CONN, CURSOR
from models.amenity import Amenity
from models.hut import Hut

import ipdb

Amenity.drop_table()
Amenity.create_table()

hot_tub = Amenity.create("Hot tub", "a toasty tub")
print(hot_tub)

Hut.drop_table()
Hut.create_table()
hut = Hut.create("brandi's hut", "washington", "north shore hut system", 13455, "some url")
hut = Hut.create("tommy's hut", "colorado", "lakewood hut system", 13455, "some url")

print(Amenity.get_all())

ipdb.set_trace()
