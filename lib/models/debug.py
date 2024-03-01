#!/usr/bin/env python3
# lib/debug.py

# from models.__init__ import CONN, CURSOR
from __init__ import CONN, CURSOR
from amenity import Amenity

import ipdb

Amenity.drop_table()
Amenity.create_table()

hot_tub = Amenity.create("Hot tub", "a toasty tub")
print(hot_tub)

# hot_tub.save()
# print(hot_tub)

ipdb.set_trace()
