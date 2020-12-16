#!/usr/bin/env python3.9
import itertools as it
from collections import defaultdict
import re
import numpy as np

constraints, yts, nts, _ = open('input').read().split('\n\n')

constraints = [list(map(int, re.findall(r'\d+', x))) for x in constraints.split('\n')]
yts = list(map(int, re.findall(r'\d+',yts)))
nts = [list(map(int, x.split(','))) for x in nts.split('\n')[1:]]

constraints = [lambda t, a=a, b=b, c=c, d=d: a<=t<=b or c<=t<=d for a,b,c,d in constraints]

ans = 0
for i, nt in enumerate(nts):
    nts[i] = [t if any(constraint(t) for constraint in constraints) else -1 for t in nt]
    ans += sum(t for t in nt if not any(constraint(t) for constraint in constraints))

print(ans)

nts = np.transpose(nts)
candidates = []
for i,col in enumerate(nts):
    candidates += [set(i for i,constraint in enumerate(constraints) if all(constraint(row) for row in col if row != -1))]

exclude = set()
while len(exclude) != len(candidates):
    for candidate in candidates:
        if len(candidate) == 1:
            exclude.update(candidate) 
            continue
        candidate -= exclude

ans = 1
for i in range(len(candidates)):
    if bool(candidates[i] & {0,1,2,3,4,5}):
        ans *= yts[i]

print(ans)