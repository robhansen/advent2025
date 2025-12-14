#!/usr/bin/env python3

import sys
from collections import deque

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

def lights_state(lights):
    return "".join([str(x) for x in lights])

def get_min_presses(target_lights, buttons):
    starting_lights = [0] * len(target_lights)
    states_seen = set(lights_state(starting_lights))

    check_queue = deque() # tuple of (lights, count)
    check_queue.append((starting_lights, 0))

    while True:
        lights, count = check_queue.popleft()
        if lights_state(lights) == lights_state(target_lights):
            return count
        if lights_state(lights) in states_seen:
            continue
        states_seen.add(lights_state(lights))
        for button in buttons:
            new_lights = lights.copy()
            for light in button:
                new_lights[light] = 1 - new_lights[light]
            check_queue.append((new_lights, count+1))
        

total_button_presses = 0
with open(sys.argv[1]) as file:
    for line in file:
        elements = line.strip().split(' ')
        target_lights = [1 if x=='#' else 0 for x in elements[0][1:-1]]
        buttons = [[int(y) for y in x[1:-1].split(',')] for x in elements[1:-1]]
        total_button_presses += get_min_presses(target_lights, buttons)

print("Total button presses = {}".format(total_button_presses))
