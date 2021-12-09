#!/usr/bin/env python3.9

import numpy as np
import itertools as it

lines = np.array([[int(x) for x in line.rstrip()] for line in open('input')])
lines = np.pad(lines, (1,1), 'constant', constant_values=(10,10))

w = np.lib.stride_tricks.sliding_window_view(lines, (3,3), writeable=True) 

m = w[:,:,1,1,None,None] < w
m[:,:,1,1] = True
i = np.where(m.all((-1,-2)))

ans = (w[(*i,1,1)] + 1).sum()
print(ans)

b = (lines < 9).astype(int)

w[(*i,1,1)] = -1
m = (lines < 0).astype(int)

parts = np.where(b & m)
parts = np.stack(parts,-1)

ans = []

# flood fill
for i in parts:
    i = tuple(i)
    seen = set()
    q = [i]
    while len(q):
        i = q.pop()
        for (dx,dy) in [(0,1), (1,0), (0,-1), (-1,0)]:
            n = (i[0] + dx, i[1] + dy)
            if lines[n] != 10 and b[n] and n not in seen:
                q.append(n)
                seen.add(n)

    ans.append(len(seen))

ans = np.prod(sorted(ans)[-3:])
print(ans)
