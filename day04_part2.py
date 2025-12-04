#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

rolls = []
with open(sys.argv[1]) as file:
    for line in file:
        rolls.append([(1 if x=='@' else 0) for x in line.strip()])

# pad right and bottom with 0s (-1 will access these elements too thanks to negative indexing)
rolls = [(x + [0]) for x in rolls]
rolls.append([0] * len(rolls[0]))

ADJACENCIES = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

iterations = 0
accessible = 0
while True:
    iterations += 1  
    removed = []
    for y in range(len(rolls)-1):
        for x in range(len(rolls[y])-1):
            if rolls[y][x]==1:
                adjacent = 0
                for location in ADJACENCIES:
                    adjacent+=rolls[y+location[1]][x+location[0]]
                if adjacent < 4:
                    removed.append((x,y))

    if len(removed) > 0:        
        for to_remove in removed:
            rolls[to_remove[1]][to_remove[0]] = 0
            accessible += 1
    else:
        break

print("After {} iterations there are {} total accessible rolls".format(iterations, accessible))
