#!/usr/bin/env python3

import sys

def is_even(num):
    return ((num % 2)==0)
def get_truncated(num):
    trunc = str(num)
    return int(trunc[0:int(len(trunc)/2)])

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

with open(sys.argv[1]) as file:
    range_strings = file.readline().strip().split(',')
    ranges = [tuple(x.split('-')) for x in range_strings]

invalid_id_sum = 0
for this_range in ranges:
    start_of_range = int(this_range[0]) if is_even(len(this_range[0])) else int('1' + '0' * len(this_range[0]))
    end_of_range = int(this_range[1]) if is_even(len(this_range[1])) else int('9' * len(this_range[0]))
    if start_of_range > end_of_range:
        continue
    trunc_start = get_truncated(start_of_range)
    trunc_end = get_truncated(end_of_range)

    for i in range(trunc_start, trunc_end+1):
        invalid_candidate = int("{}{}".format(i,i))
        if invalid_candidate >= start_of_range and invalid_candidate <= end_of_range:
            print("invalid id {}".format(invalid_candidate))
            invalid_id_sum += invalid_candidate

print("Sum of invalid ids: {}".format(invalid_id_sum))
