#!/usr/bin/env python3

import sys

def is_divisible_by(len, divisible_by):
    return ((len % divisible_by)==0)

def get_len_divisible_by(len, divisible_by, round_up):
    while True:
        if is_divisible_by(len,divisible_by):
            return len
        len += 1 if round_up else -1
        if len==0:
            return len    

def get_truncated(num, repititions):
    trunc = str(num)
    return int(trunc[0:int(len(trunc)/repititions)])

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

with open(sys.argv[1]) as file:
    range_strings = file.readline().strip().split(',')
    ranges = [tuple(x.split('-')) for x in range_strings]

invalid_ids = set()
for this_range in ranges:
    for repititions in range(2, len(this_range[1])+1):
        start_of_range = int(this_range[0]) if is_divisible_by(len(this_range[0]), repititions) else int('1' + '0' * (get_len_divisible_by(len(this_range[0]), repititions, True)-1))
        end_of_range = int(this_range[1]) if is_divisible_by(len(this_range[1]), repititions) else int('9' * (get_len_divisible_by(len(this_range[1]), repititions, False)))
        if start_of_range > end_of_range:
            continue
        trunc_start = get_truncated(start_of_range, repititions)
        trunc_end = get_truncated(end_of_range, repititions)

        for i in range(trunc_start, trunc_end+1):
            invalid_candidate = int(str(i)*repititions)
            if invalid_candidate >= start_of_range and invalid_candidate <= end_of_range:
                print("invalid id {}".format(invalid_candidate))
                invalid_ids.add(invalid_candidate)

print("Sum of invalid ids: {}".format(sum(invalid_ids)))
