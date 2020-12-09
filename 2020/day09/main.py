#!/usr/bin/env python3.9
import itertools as it

program = [int(line.rstrip()) for line in open('in1')]

invalid = 0

for i, line in enumerate(program[25:]):
    if not any(x+y == line for x,y in it.combinations(program[i:i+25], 2)):
        invalid = line
        break

print(invalid)

_range = range(2, len(program))
for x,y in it.product(_range, _range):
    if sum(program[x:y]) == invalid:
        r = program[x:y]
        print(min(r) + max(r))
        break
