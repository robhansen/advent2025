#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

rolls = []
with open(sys.argv[1]) as file:
    for line in file:
        rolls.append([(1 if x=='@' else 0) for x in line.strip()])

# pad right and bottom with 0s (-1 will access these elements too)
rolls = [(x + [0]) for x in rolls]
rolls.append([0] * len(rolls[0]))

ADJACENCIES = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

accessible = 0
for y in range(len(rolls)-1):
    map = ""
    for x in range(len(rolls[y])-1):
        if rolls[y][x]==1:
            adjacent = 0
            for location in ADJACENCIES:
                #print(y+location[1], x+location[0])
                adjacent+=rolls[y+location[1]][x+location[0]]
                if rolls[y+location[1]][x+location[0]]==1:
                    if y+location[1]==-1 or x+location[0]==-1:
                        print("oops - found 1 at negative location")
            accessible += 1 if adjacent < 4 else 0
            map += "x" if adjacent < 4 else "@"
        else:
            map += "."
    print(map)

print("There are {} accessible rolls".format(accessible))
