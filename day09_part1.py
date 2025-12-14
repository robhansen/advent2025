#!/usr/bin/env python3

import sys
from collections import defaultdict

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

tiles = []
with open(sys.argv[1]) as file:
    for line in file:
        tiles.append(tuple([int(x) for x in line.strip().split(',')]))

largest_area = 0
for i in range(len(tiles)):
    for j in range(len(tiles)):
        area = (abs(tiles[i][0] - tiles[j][0])+1) * (abs(tiles[i][1] - tiles[j][1])+1)
        if area > largest_area:
            largest_area = area

print("Largest area: {}".format(largest_area))
