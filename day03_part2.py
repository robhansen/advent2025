#!/usr/bin/env python3

import sys

NUM_BATTERIES = 12

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

total_joltage = 0
with open(sys.argv[1]) as file:
    for line in file:
        values = [int(x) for x in line.strip()]
        high_values = []
        for i in range(NUM_BATTERIES):
            start_index = high_values[-1][1]+1 if len(high_values) > 0 else 0
            high_value = [0,0] # value and index
            for j in range(start_index, len(values)+1-(NUM_BATTERIES-i)):
                if values[j] > high_value[0]:
                    high_value = [values[j], j]
            high_values.append(high_value)
        joltage_string = ""
        for high_value in high_values:
            joltage_string += str(high_value[0])
        joltage = int(joltage_string)
        total_joltage += joltage

print("Total joltage: {}".format(total_joltage))
                

