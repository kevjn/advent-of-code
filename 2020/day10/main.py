#!/usr/bin/env python3.9
import itertools as it
from math import factorial

adaptors = [int(line.rstrip()) for line in open('in1')]

adaptors += [0]
adaptors = sorted(adaptors)
adaptors += [adaptors[-1] + 3]

_1, _3 = 0,0

for i in range(len(adaptors)-1):
    diff = adaptors[i+1] - adaptors[i]
    _1 += diff == 1
    _3 += diff == 3

cache = {}
def calc(i):
    if i in cache:
        return cache[i]

    if i+1 >= len(adaptors):
        return 1

    ans = 0
    for j in range(i+1, len(adaptors)):
        if adaptors[j] - adaptors[i] <= 3:
            ans += calc(j)
    
    cache[i] = ans
    return ans

print(_1 * _3)

print(calc(0))

