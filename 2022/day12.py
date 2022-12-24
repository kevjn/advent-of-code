#!/usr/bin/env python3.10

import numpy as np

m = np.array([list(map(ord,line.rstrip())) for line in open("input").readlines()])
m = m - ord('a') + 1
start = np.array(np.where(m == -13)).flatten()
end = np.array(np.where(m == -27)).flatten()

m[tuple(start)] = 0
m[tuple(end)] = 26

for p1 in [True, False]:
    nx = [start]
    steps = np.full_like(m, 1e3, dtype=int)
    steps[tuple(start)] = 0
    while nx:
        cur = nx.pop()
        for dxdy in map(np.array,[(0,1), (1,0), (0,-1), (-1,0)]):
            n = cur + dxdy
            key = tuple(n)

            try:
                if (n < 0).any():
                    continue

                if m[key] > m[tuple(cur)] + 1:
                    continue

                s = steps[tuple(cur)] + 1
                if s >= steps[key]:
                    continue

                if m[key] == 1 and not p1:
                    s -= 1

                steps[key] = s
                nx.append(n)
            except IndexError:
                continue

    print(steps[tuple(end)])
