#!/usr/bin/env python3

# Be warned, this is *not* a good implementation - it does run and get the right answer but it takes a very long time

import sys
from collections import defaultdict
import numpy as np
from skimage.morphology import flood_fill

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

red_tiles = []
with open(sys.argv[1]) as file:
    for line in file:
        red_tiles.append(tuple([int(x) for x in line.strip().split(',')]))

# since the absolute red tile positions don't matter adjust them to start at 1,1
min_tile_positions = (min(red_tiles, key=lambda x: x[0])[0], min(red_tiles, key=lambda x: x[1])[1])

for i in range(len(red_tiles)):
    red_tiles[i] = (red_tiles[i][0] - (min_tile_positions[0]-1), red_tiles[i][1] - (min_tile_positions[1]-1))

max_map = (max(red_tiles, key=lambda x: x[1])[1], max(red_tiles, key=lambda x: x[0])[0])
max_map = (max_map[0] + 2, max_map[1] + 2) # allow border of 1 at bottom and right for flood fill
print("Map size: {}".format(max_map))
map_array = np.ones(max_map, dtype=np.uint8)

for i in range(len(red_tiles)):
    map_array[red_tiles[i][1], red_tiles[i][0]] = 2
    j = (i+1) % len(red_tiles) # modulo to wrap the last one back to 0
    deltas = [0,0]
    if red_tiles[i][0] != red_tiles[j][0]:
        deltas[0] = 1 if red_tiles[i][0] < red_tiles[j][0] else -1
    if red_tiles[i][1] != red_tiles[j][1]:
        deltas[1] = 1 if red_tiles[i][1] < red_tiles[j][1] else -1

    start = list(red_tiles[i])
    while start != list(red_tiles[j]):
        map_array[start[1], start[0]] = 2
        start[0] += deltas[0]
        start[1] += deltas[1]

assert map_array[0][0] == 1
print("Doing flood fill of outside")
flood_fill(map_array, (0, 0), 0, connectivity=1, in_place=True)
map_array = map_array.astype(np.bool_) # squash to bool so both 1s and 2s become true, 0s are false
print("Map constructed - checking areas")

largest_area = 0
for i in range(len(red_tiles)):
    for j in range(i+1, len(red_tiles)):
        area = (abs(red_tiles[i][0] - red_tiles[j][0])+1) * (abs(red_tiles[i][1] - red_tiles[j][1])+1)
        if area > largest_area:
            # check everything encompassed is True
            section = map_array[min(red_tiles[i][1], red_tiles[j][1]):max(red_tiles[i][1]+1, red_tiles[j][1]+1), min(red_tiles[i][0], red_tiles[j][0]):max(red_tiles[i][0]+1, red_tiles[j][0]+1)]
            if np.all(section):
                largest_area = area

print("Largest valid area: {}".format(largest_area))

