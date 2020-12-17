#!/usr/bin/env python3.9
import itertools as it
from collections import defaultdict
import re
import numpy as np
from operator import add

lines = [line.rstrip() for line in open('input')]

active = set()

for y,line in enumerate(lines):
    for x, cell in enumerate(line):
        if cell == '#':
            active.add((x,y,0,0))

i = -1
while (i := i + 1) < 6:
    new_active = set()
    for x, y, z, w in it.product(range(-12,12), repeat=4):
        active_nbrs = 0
        for dx, dy, dz, dw in it.product(range(-1,2), repeat=4):
            if (dx,dy,dz,dw) != (0,0,0,0):
                active_nbrs += (x+dx, y+dy, z+dz, w+dw) in active

        if ((x,y,z,w) not in active and active_nbrs == 3)\
            or ((x,y,z,w) in active and active_nbrs in (2,3)):

                new_active.add((x,y,z,w))

    active = new_active

print(len(active))