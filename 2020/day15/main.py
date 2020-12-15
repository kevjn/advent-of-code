#!/usr/bin/env python3.9
import itertools as it
from collections import defaultdict

line = next([int(x) for x in x.rstrip().split(',')] for x in open('in1'))
spoken = defaultdict(list, {x:[i] for i,x in enumerate(line, 1)})
nth = 30000000

last = line[-1]
for i in range(len(line)+1, nth+1):
    if len(spoken[last]) < 2: # .count?
        spoken[0].append(i)
        last = 0
    else:
        d = spoken[last][-1] - spoken[last][-2]
        spoken[d].append(i)
        last = d

print(last)