#!/usr/bin/env python3.10

import numpy as np

def f(x1y1, x2y2):
    (x1,y1), (x2,y2) = x1y1, x2y2
    if x1 == x2:
        s = np.sign(y2-y1)
        return set([(x1,y) for y in range(y1,y2+s, s)])
    else:
        s = np.sign(x2-x1)
        return set([(x,y1) for x in range(x1,x2+s, s)])

paths = [x.rstrip() for x in open("input").readlines()]
paths = [[tuple(map(int,y.split(','))) for y in x] for x in [x.split(' -> ') for x in paths]]
paths = [[f(*a) for a in zip(p, p[1:])] for p in paths]
paths = set.union(*sum(paths, []))

origin = (500,0)
transit = None
sand = set()
floor_y = max(y for (x,y) in paths)+1
first = None

while True:
    if transit is None:
        transit = np.array(origin)
    
    if transit[1] != floor_y:
        for dx in [(0,1), (-1,1), (1,1)]:
            nx = transit + dx
            if tuple(nx) not in paths:
                transit = nx
                break
        else:
            sand.add(tuple(transit))
            paths.add(tuple(transit))
            if tuple(transit) == origin:
                print(len(sand))
                break
            transit = None
    else:
        if first is None:
            print(len(sand))
            first = transit
        sand.add(tuple(transit))
        paths.add(tuple(transit))
        transit = None