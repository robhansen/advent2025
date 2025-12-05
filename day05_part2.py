#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

fresh_ranges = []
with open(sys.argv[1]) as file:
    for line in file:
        if line.strip()=="":
            break
        fresh_ranges.append([int(x) for x in line.strip().split('-')])

for i in range(len(fresh_ranges)):
    this_range = fresh_ranges[i]
    for j in range(i+1, len(fresh_ranges)):
        if (this_range[0] <= fresh_ranges[j][1] and this_range[1] >= fresh_ranges[j][0]): # the two ranges overlap
            fresh_ranges[j] = [min(this_range[0], fresh_ranges[j][0]), max(this_range[1], fresh_ranges[j][1])]
            fresh_ranges[i] = None
            break

fresh_ids = 0
for this_range in fresh_ranges:
    if this_range is not None:
        fresh_ids += (1+this_range[1]-this_range[0])

print("There are {} fresh ingredient IDs".format(fresh_ids))
