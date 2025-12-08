#!/usr/bin/env python3

import sys
from collections import defaultdict

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

nodes = []
with open(sys.argv[1]) as file:
    for line in file:
        nodes.append(tuple([int(x) for x in line.strip().split(',')]))

edges = []
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        dist = ((nodes[i][0]-nodes[j][0])**2 + (nodes[i][1]-nodes[j][1])**2 + (nodes[i][2]-nodes[j][2])**2)**0.5
        edges.append((dist, i, j))

edges.sort(key=lambda x: x[0])

num_circuits_to_make = 1000 if len(edges) > 1000 else 10 # make 10 circuits for verification data, make 1000 for real input

circuit_indexes = [None] * len(nodes)
next_circuit_index = 0
for i in range(num_circuits_to_make):
    edge = edges[i]
    if circuit_indexes[edge[1]] is None and circuit_indexes[edge[2]] is None: # neither node is part of a circuit yet, assign them to a new circuit
       circuit_indexes[edge[1]] = next_circuit_index
       circuit_indexes[edge[2]] = next_circuit_index
       next_circuit_index += 1
    elif circuit_indexes[edge[1]] is None: # add the node not in a circuit to the one that is
        circuit_indexes[edge[1]] = circuit_indexes[edge[2]]
    elif circuit_indexes[edge[2]] is None: # add the node not in a circuit to the one that is
        circuit_indexes[edge[2]] = circuit_indexes[edge[1]]
    else:
        # both nodes are already part of a circuit - join them together if they are not in the same circuit
        if circuit_indexes[edge[1]] != circuit_indexes[edge[2]]:
            # merge the two circuits
            index_to_replace = circuit_indexes[edge[2]]
            for j in range(len(circuit_indexes)):
                if circuit_indexes[j] == index_to_replace:
                    circuit_indexes[j] = circuit_indexes[edge[1]]

circuit_sizes = defaultdict(int)
for circuit_index in circuit_indexes:
    if circuit_index is not None:
        circuit_sizes[circuit_index] += 1
circuit_sizes_list = [list(circuit_sizes.values())[i] for i in range(len(circuit_sizes))]
circuit_sizes_list.sort(reverse=True)

print("After creating {} connections there are {} circuits of 2 or more boxes; the three largest multiply to {}".format(num_circuits_to_make, len(circuit_sizes_list), circuit_sizes_list[0]*circuit_sizes_list[1]*circuit_sizes_list[2]))
