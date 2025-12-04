#!/usr/bin/env python3

STARTING_POSITION = 50
NUM_POSITIONS = 100

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

position = STARTING_POSITION
zero_count = 0
with open(sys.argv[1]) as file:
    for line in file:
        move = int(line[1:].strip())
        position = position+move if line[0]=='R' else position-move
        position = position % NUM_POSITIONS
        if position == 0:
            zero_count+=1

print("The dial pointed to 0 {} times".format(zero_count))
