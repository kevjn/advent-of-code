#!/usr/bin/env python3.9

import numpy as np

lines = open('input').read().rstrip().replace('.','0').replace('>','1').replace('v','2')
grid = np.array([[int(x) for x in line] for line in lines.split('\n')])

for step in range(1, int(1e9)):
    y,x = np.where(grid == 1)
    nx = (x + 1) % grid.shape[1]
    mx = grid[y, nx] == 0

    grid[y[mx], nx[mx]] = 1
    grid[y[mx], x[mx]] = 0

    y,x = np.where(grid == 2)
    ny = (y + 1) % grid.shape[0]
    my = grid[ny, x] == 0
    grid[ny[my], x[my]] = 2
    grid[y[my], x[my]] = 0

    if not any(mx) and not any(my):
        break

print(step)