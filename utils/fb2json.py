#!/usr/bin/env python

from __future__ import print_function
import json
import sys
from pprint import PrettyPrinter

"""
Parse FB history of locations to a bunch of coordinates, timestamp
"""

with open(sys.argv[1], 'r') as jf:
        data = json.loads(jf.read())

K0='location_history'
K1='attachments'
K2='data'
K3='place'

pp = PrettyPrinter(indent=2)

if K0 not in data:
    print("Input data does not contain key %s" % K0)
    sys.exit(1)

if len(data[K0]) == 0:
    print("There is no history of locations")
    sys.exit(1)


for loc_hist in data[K0]:
    for attachment in loc_hist[K1]:
        for place in attachment[K2]:
            print(json.dumps(place[K3]))
