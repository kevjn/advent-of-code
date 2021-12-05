#!/usr/bin/env python3.9

import numpy as np

lines = [line.rstrip() for line in open('input')]

seen = set()
ans = set()

for line in lines:
    a,b = line.split('->')
    x1,y1 = map(int, a.split(','))
    x2,y2 = map(int, b.split(','))

    dx, dy = map(np.sign, (x2-x1, y2-y1))

    nx, ny = x1,y1
    l = [(nx,ny)]
    while (nx,ny) != (x2,y2):
        nx += dx
        ny += dy
        l.append((nx,ny))

    ans |= (set(l) & seen)
    seen |= set(l)

print(len(ans))