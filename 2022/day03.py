#!/usr/bin/env python3.10

import numpy as np

lc = {chr(x): x-96 for x in range(ord('a'), ord('z')+1)}
uc = {chr(x): x-64+26 for x in range(ord('A'), ord('Z')+1)}
t = lc | uc

lines = [np.array([t[c] for c in line.rstrip()]) for line in open("input")]

print(sum(a[np.in1d(a,b)][0] for (a,b) in [np.split(line, 2) for line in lines]))

print(sum(a[np.in1d(a,b) & np.in1d(a,c)][0] for (a,b,c) in [lines[i:i+3] for i in range(0, len(lines), 3)]))