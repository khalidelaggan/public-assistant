#!/usr/bin/env python
from lib.dir import Directions

origin = "sunset park, las vegas"
destination = "UNLV, las vegas"
directions = Directions(origin, destination)

for instruction in directions.instructions:
    print instruction

print "You will walk for {}, in {}".format(directions.distance['text'], directions.duration['text'])
