#!/usr/bin/env python3.9

import numpy as np

lines = np.array([[int(x) for x in line.rstrip()] for line in open('input')])
lines = np.pad(lines, (1,1), 'constant', constant_values=-1)
ws = np.lib.stride_tricks.sliding_window_view(lines, (3,3), writeable=True)

p1 = 0
for i in range(10_000):
    lines[lines != -1] += 1
    seen = set()
    while (lines > 9).any():
        flash = np.where(ws[:,:,1,1] > 9)
        f = np.stack(flash,-1)
        f = set(map(tuple, f.tolist()))
        seen |= f

        for x,y in f:
            ws[x,y] += ws[x,y] != -1

        for x,y in f:
            ws[x,y,1,1] = 0

    p1 += len(seen) * (i < 100)
    for x,y in seen:
        ws[x,y,1,1] = 0

    if len(seen) == 10*10:
        p2 = i+1
        break

print(p1)
print(p2)