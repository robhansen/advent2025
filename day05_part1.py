#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

fresh = 0
fresh_ranges = []
got_fresh_ranges = False
with open(sys.argv[1]) as file:
    for line in file:
        if line.strip()=="":
            got_fresh_ranges = True
            continue
        
        if not got_fresh_ranges:
            fresh_ranges.append(tuple([int(x) for x in line.strip().split('-')]))
        else:
            ingredient = int(line.strip())
            for this_range in fresh_ranges:
                if ingredient >= this_range[0] and ingredient <= this_range[1]:
                    fresh += 1
                    break

print("Found {} fresh ingredients".format(fresh))
