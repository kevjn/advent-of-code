#!/usr/bin/env python3.9
import itertools as it
from math import factorial

lines = ['x' + line.rstrip() + 'x' for line in open('in2')]

lines.insert(0, 'x' * len(lines[0]))
lines += ['x' * len(lines[0])]

change = True
while change:
    new_lines = []
    for i in range(1, len(lines)-1):
        line = lines[i]
        new_line = ""
        for j in range(1, len(lines[i])-1):
            seat = lines[i][j]

            directions = list(it.product((-1, 0, 1), repeat=2))
            directions.remove((0,0))

            adjacent = []
            for d in directions:
                _i, _j = i,j
                while True:
                    _i += d[0]
                    _j += d[1]
                    s = lines[_i][_j]
                    if s != '.':
                        break
                    
                adjacent += s

            if seat == 'L' and '#' not in adjacent:
                new_line += '#'
                continue

            if seat == '#' and adjacent.count('#') >= 5:
                new_line += 'L'
                continue

            new_line += seat

        new_lines += ['x' + new_line + 'x']

    new_lines.insert(0, 'x' * len(lines[0]))
    new_lines += ['x' * len(lines[0])]

    change = new_lines != lines
    lines = new_lines


ans = 0
for seat in "".join(lines):
    ans += seat == '#'

print(ans)
