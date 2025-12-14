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

def evaluated_name(node, dac_seen, fft_seen):
    return "{}{}{}".format(node, 1 if dac_seen else 0, 1 if fft_seen else 0)

def check_path(current_node, dac_seen, fft_seen, nodes, post_dac, post_fft, evaluated_nodes):
    if current_node == "dac":
        dac_seen = True
    elif current_node == "fft":
        fft_seen = True
    elif current_node == "out":
        return 1 if fft_seen and dac_seen else 0
    
    # if this node has ever been seen in a path after dac/fft, then if it hasn't seen that node yet we can abort now
    if dac_seen:
        post_dac.add(current_node)
    elif current_node in post_dac:
        return 0
    if fft_seen:
        post_fft.add(current_node)
    elif current_node in post_fft:
        return 0
    
    eval_name = evaluated_name(current_node, dac_seen, fft_seen)
    if eval_name in evaluated_nodes:
        return evaluated_nodes[eval_name]
    
    successful_paths = 0
    for node in nodes.get(current_node, []):
        successful_paths += check_path(node, dac_seen, fft_seen, nodes, post_dac, post_fft, evaluated_nodes)
    evaluated_nodes[eval_name] = successful_paths
    return successful_paths

print("There are {} paths to the exit that visit 'dac' and 'fft'".format(check_path("svr", False, False, nodes, set(), set(), {})))
