#!/usr/bin/env python3.9

import re
import itertools as it

line = open('input').readline().rstrip()

x1,x2, y1,y2 = map(int, re.findall(r'(-?\d+)', line))

v = {}

for dx,dy in it.product(range(1,x2+1), range(y1, -y1)):
    x,y = 0,0
    best = 0
    key = dx,dy
    while x <= x2 and y > y1:
        x,y = x + dx, y + dy
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        dy -= 1
        best = max(best, y)
        if x1 <= x <= x2 and y1 <= y <= y2:
            v[key] = best
            break

print(max(v.values()))
print(len(v))