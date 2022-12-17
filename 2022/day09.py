#!/usr/bin/env python3.10

import numpy as np

lines = map(str.rstrip, open("input").readlines())

num_knots = 10
heads = [(0,0)] * num_knots
knots = [{(0,0)} for _ in range(num_knots)]

directions = {
    'R': (1,0),
    'L': (-1,0),
    'U': (0,1),
    'D': (0,-1)
}

def is_adjacent(a,b):
    x,y = a
    for dx,dy in [(0,0), (0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]:
        if (x + dx, y + dy) == b:
            return True
    return False

for inst in lines:
    d = directions[inst[0]]
    n = inst[1:]

    for _ in range(int(n)):
        heads[-1] = (heads[-1][0] + d[0], heads[-1][1] + d[1])

        for i,j in zip(range(num_knots-2,-1,-1),range(num_knots-1,-1,-1)):
            back,front = heads[i], heads[j]
            if not is_adjacent(front,back):
                dxdy = np.sign(np.array(front) - np.array(back))
                heads[i] = tuple(np.array(back) + dxdy)
                knots[i].add(heads[i])

print(len(knots[-2]))
print(len(knots[0]))