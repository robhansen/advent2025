#!/usr/bin/env python3

import sys
from collections import defaultdict

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

arrangement = []
with open(sys.argv[1]) as file:
    for line in file:
        arrangement.append(line.strip())

beams = {arrangement[0].index('S'): 1}
for i in range(1, len(arrangement)):
    new_beams = defaultdict(int)
    for beam_index, count in beams.items():    
        if arrangement[i][beam_index] == '^':
            new_beams[beam_index-1] += count
            new_beams[beam_index+1] += count
        else:
            new_beams[beam_index] += count
    beams = new_beams

print("The tachyon beam can be in 1 of {} possible timelines.".format(sum(beams.values())))
