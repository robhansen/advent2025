#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

arrangement = []
with open(sys.argv[1]) as file:
    for line in file:
        arrangement.append(line.strip())

beams = [arrangement[0].index('S')]
splits = 0
for i in range(1, len(arrangement)):
    new_beams = set()
    for beam in beams:
        if arrangement[i][beam] == '^':
            new_beams.add(beam-1)
            new_beams.add(beam+1)
            splits += 1
        else:
            new_beams.add(beam)
    beams = new_beams

print("The tachyon beam undergoes {} splits.".format(splits))
