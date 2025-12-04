#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

high_joltage = 0
with open(sys.argv[1]) as file:
    for line in file:
        values = [int(x) for x in line.strip()]
        high_val = [0,0] # value and index
        for i in range(0, len(values)-1):
            if values[i] > high_val[0]:
                high_val = [values[i], i]
        low_val = [0,0]
        for i in range(high_val[1]+1, len(values)):
            if values[i] > low_val[0]:
                low_val = [values[i], i]
        joltage = int("{}{}".format(high_val[0],low_val[0]))
        print(joltage)
        high_joltage += joltage

print("Total joltage: {}".format(high_joltage))
