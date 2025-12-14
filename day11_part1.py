#!/usr/bin/env python3

import sys
from collections import deque

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

nodes = {}
with open(sys.argv[1]) as file:
    for line in file:
        nodes[line[0:3]] = line[4:].strip().split(' ')

def check_path(current_node, nodes):
    if current_node == "out":
        return 1
    else:
        successful_paths = 0
        for node in nodes.get(current_node, []):
            successful_paths += check_path(node, nodes)
        return successful_paths

print("There are {} paths to the exit".format(check_path("you", nodes)))
