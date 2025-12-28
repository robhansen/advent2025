#!/usr/bin/env python3

# This doesn't work on the validation data but does on the real input, which is a bit rubbish...

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

fits = 0
num_blocks = []
requirements = []
with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        if len(line)<3:
            if len(line)>0:
                num_blocks.append(0)
            continue
        if len(line)> 3:
            tokens = line.split()
            area = [int(x) for x in tokens[0][:-1].split('x')]
            requirements = [int(x) for x in tokens[1:]]
            max_size = sum(requirements)*9
            min_size = 0
            for i in range(len(requirements)):
                min_size += requirements[i]*num_blocks[i]
            if area[0]*area[1] >= max_size:
                fits += 1
            elif area[0]*area[1] > min_size:
                raise Exception("This *may* fit via interlocking")

        else:
            num_blocks[-1] += sum([1 if x=='#' else 0 for x in line])

print("{} regions can definitely fit the presents".format(fits))
