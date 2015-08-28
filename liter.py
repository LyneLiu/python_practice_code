#! /usr/bin/env python
# @author:lyne

tank_size = int(raw_input("Size of tank:"))
percent_full = int(raw_input("Percent full:"))
liter_per_km = int(raw_input("km per liter:"))
gas_kms = 200

travel_kms = tank_size * percent_full * liter_per_km / 100
if travel_kms > gas_kms:
    print "You can go another %d km.\nThe next gas station is %d km away.\nYou can wait the next station." % (travel_kms,gas_kms)
else:
    print "You can go another %d km.\nThe next gas station is %d km away.\nGet gas now!" % (travel_kms,gas_kms)
