#!/usr/bin/env python3.9

from collections import defaultdict
import re
import numpy as np

template, lines = open('input').read().split('\n\n')

cat = lambda a,b: int(str(ord(a)) + str(ord(b)))

pairs = []
values = []
for pair in lines.rstrip().split('\n'):
    a,b,c = re.findall(r'([A-Z])', pair)

    pairs.append(cat(a,b))
    values.append((cat(a,c), cat(c,b)))

values = np.array(values)
pairs = np.array(pairs)

ply = [cat(x,y) for x,y in zip(template, template[1:])]
ply = np.bincount(ply, minlength=max(pairs)+1)

ans = defaultdict(int)
for c in template: ans[c] += 1

for step in range(1,41):
    m = ply[pairs]
    indices = np.where(m)[0]

    for i, (x,y) in enumerate(values[indices]):
        i = indices[i]
        ply[x] += m[i]
        ply[y] += m[i]
        ply[pairs[i]] -= m[i]
        c = chr(int(str(values[i][0])[2:]))
        ans[c] += m[i]

    v = ans.values()
    print(step, max(v) - min(v))