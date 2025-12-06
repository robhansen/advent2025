#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

values = []
with open(sys.argv[1]) as file:
    for line in file:
        values.append(line.strip('\n').strip('\r'))

total = 0
current_values = []
for i in range(len(values[0])-1, -1, -1): # work backwards so that when we hit the operator we know we're at the end of the operation
    value_string = ""
    for j in range(len(values)-1): # final row is the operators
        if values[j][i]!=' ':
            value_string += values[j][i]
    if value_string=="":
        continue
    current_values.append(int(value_string))

    if values[-1][i]!=' ':
        if values[-1][i] == '*':
            res = 1
            for val in current_values:
                res *= val
            total += res
        else:
            total += sum(current_values)
        current_values = []

print("The sum of all operations is {}".format(total))
