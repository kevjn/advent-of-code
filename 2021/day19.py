#!/usr/bin/env python3.9

import itertools as it
import numpy as np
import re

class Scanner:
    def __init__(self, id, xyz):
        self.id = id
        self.xyz = np.array(xyz, dtype=int)
        self.pos = None

    def __eq__(self, other):
        return self.id == other.id

lines = [line for line in open('example').read().split('\n\n')]
lines = [line.rstrip().split('\n')[1:] for line in lines]
scanners = [Scanner(i, [(tuple(map(int, re.findall(r'(-?\d+)', xyz)))) for xyz in line]) for i,line in enumerate(lines)]

scanners[0].dir = (1,1,1)
scanners[0].face = (0,1,2)
scanners[0].pos = (0,0,0)
scanners[0].beacons = set(list(map(tuple, scanners[0].xyz.tolist())))

while not all(s.pos for s in scanners):
    for a,b in it.product(scanners, scanners):
        if a.pos and not b.pos:
            for dir in it.product([1,-1], [1,-1], [1,-1]):
                for face in it.permutations([0,1,2]):
                    rot = (b.xyz * dir)[:,face]
                    for origin in a.xyz:
                        translations = rot + (origin - rot)[:,None]
                        mask = np.isin(translations, a.xyz).all(-1)
                        if (mask.sum(-1) > 11).any():
                            i = mask.sum(-1).argmax()
                            pos = (translations[i] - rot)[0]

                            bns = translations[i]
                            bns = a.pos + (bns * np.array(a.dir)[list(a.face)])[:,a.face]

                            if not b.pos:
                                b.pos = tuple(a.pos + (pos * np.array(a.dir)[list(a.face)])[list(a.face)])
                                b.dir = dir
                                b.face = face
                                b.beacons = set(list(map(tuple, bns.tolist())))
                            break

beacons = set.union(*(s.beacons for s in scanners))
p1 = len(beacons)
print(p1)

p = np.array([s.pos for s in scanners])
p2 = np.abs(p[:,None] - p).sum(-1).max()
print(p2)