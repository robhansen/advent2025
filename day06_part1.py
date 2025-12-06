#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

values = []
with open(sys.argv[1]) as file:
    for line in file:
        values.append(line.strip().split())

print("Got {} sets of {} numbers".format(len(values[0]), len(values)-1))
total = 0
for i in range(len(values[0])):
    vals = []
    for j in range(len(values)-1): # final row is the operators
        vals.append(int(values[j][i]))
    if values[-1][i] == '*':
        res = 1
        for val in vals:
            res *= val
        total += res
    else:
        total += sum(vals)

print("The sum of all operations is {}".format(total))
