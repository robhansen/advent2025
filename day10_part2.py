#!/usr/bin/env python3

import sys
import numpy as np
from scipy.optimize import milp, LinearConstraint

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

total_button_presses = 0
with open(sys.argv[1]) as file:
    for line in file:
        elements = line.strip().split(' ')
        joltage_levels = [int(x) for x in elements[-1][1:-1].split(',')]
        buttons = [[int(y) for y in x[1:-1].split(',')] for x in elements[1:-1]]
        A = np.zeros((len(joltage_levels), len(buttons)))
        for i in range(len(buttons)):
            for val in buttons[i]:
                A[val, i] = 1
        c = np.ones(A.shape[1])
        B = LinearConstraint(A, lb=joltage_levels, ub=joltage_levels)
        total_button_presses += int(sum(milp(c, integrality=c, constraints=B).x))

print("Total button presses = {}".format(total_button_presses))
