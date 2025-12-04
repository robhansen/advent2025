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
        move = move if line[0]=='R' else (0-move)
        while True:
            # move one click
            if move > 0:
                position += 1
                move -= 1
                if position >= NUM_POSITIONS:
                    position = 0
            elif move < 0:
                position -= 1
                move += 1
                if position < 0:
                    position = NUM_POSITIONS-1
            
            # check if we're at 0
            if position == 0:
                zero_count += 1

            # are we done with moving?
            if move == 0:
                break

print("The dial pointed to 0 {} times during the move".format(zero_count))
