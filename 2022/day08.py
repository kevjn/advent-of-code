#!/usr/bin/env python3.10

import numpy as np

trees = np.array([list(map(int, x.rstrip())) for x in open("input")])

f = lambda t: np.diff(np.maximum.accumulate(t[1:-1], 1), 1) > 0

left = f(trees[:, :-1])
top = f(trees.T[:, :-1]).T
right = f(trees[:, 1:][:,::-1])[:,::-1]
bot = f(trees.T[:, 1:][:,::-1])[:,::-1].T

ans = (right | left | top | bot).sum() + (trees.shape[0]*4)-4
print(ans)

ans = np.ones_like(trees)
for _ in range(4):
    for (x,y) in np.ndindex(trees.shape):
        a = trees[x, y+1:] < trees[x,y]
        ans[x,y] *= len(a) if a.all() else a.argmin()+1

    ans = np.rot90(ans)
    trees = np.rot90(trees)

print(ans.max())