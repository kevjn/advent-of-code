#!/usr/bin/env python
import itertools as it
import re
from operator import add
from collections import defaultdict

lines = [line.rstrip() for line in open('input')]

_dir = {'e': (1,0), 'se': (0.5,-1), 'sw': (-0.5,-1), 'w': (-1,0), 'nw': (-0.5,1), 'ne': (0.5,1)}

tiles = set()

for line in lines:
    d = (_dir[d] for d in re.findall(r'(e|se|sw|w|nw|ne)',line))
    tile = tuple(map(sum, zip(*d)))
    if tile in tiles:
        tiles.remove(tile)
    else:
        tiles.add(tile)

print(len(tiles))

for _ in range(100):
    new_tiles = tiles.copy()
    black_nbrs = defaultdict(int)
    for tile in tiles:
        nbrs = [tuple(map(add,tile,d)) for d in _dir.values()]
        if sum(nbr in tiles for nbr in nbrs) not in [1,2]:
            new_tiles.remove(tile)

        for nbr in nbrs:
            black_nbrs[nbr] += 1
    
    for nbr,val in black_nbrs.items():
        if val == 2:
            new_tiles.add(nbr)

    tiles = new_tiles

print(len(tiles))