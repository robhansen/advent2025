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

circuits = {}
circuit_indexes = [None] * len(nodes)
next_circuit_index = 0
for i in range(len(edges)):
    edge = edges[i]
    if circuit_indexes[edge[1]] is None and circuit_indexes[edge[2]] is None: # neither node is part of a circuit yet, assign them to a new circuit
       circuit_indexes[edge[1]] = next_circuit_index
       circuit_indexes[edge[2]] = next_circuit_index
       circuits[next_circuit_index] = 2
       next_circuit_index += 1
    elif circuit_indexes[edge[1]] is None: # add the node not in a circuit to the one that is
        circuit_indexes[edge[1]] = circuit_indexes[edge[2]]
        circuits[ circuit_indexes[edge[2]]] += 1
    elif circuit_indexes[edge[2]] is None: # add the node not in a circuit to the one that is
        circuit_indexes[edge[2]] = circuit_indexes[edge[1]]
        circuits[ circuit_indexes[edge[1]]] += 1
    else:
        # both nodes are already part of a circuit - join them together if they are not in the same circuit
        if circuit_indexes[edge[1]] != circuit_indexes[edge[2]]:
            # merge the two circuits
            index_to_replace = circuit_indexes[edge[2]]
            for j in range(len(circuit_indexes)):
                if circuit_indexes[j] == index_to_replace:
                    circuit_indexes[j] = circuit_indexes[edge[1]]
                    circuits[circuit_indexes[edge[1]]] += 1
            del circuits[index_to_replace]
    if len(circuits) == 1 and circuits[list(circuits.keys())[0]] >= len(nodes):
        print("Connecting {} and {} brings all boxes into a single circuit: the x coordinates multiply to {}".format(nodes[edge[1]], nodes[edge[2]], nodes[edge[1]][0]*nodes[edge[2]][0]))
        break

