#!/usr/bin/env python3.9

import numpy as np
import itertools as it

lines = [line.rstrip() for line in open('input')]

digits = [
    'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 
    'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'
]

alpha = lambda d: [ord(x) - ord('a') for x in d]
digitize = lambda digits: np.array([np.bincount(alpha(d), minlength=7) for d in digits])

bins = digitize(digits)

p1, p2 = 0,0
for line in lines:
    a, b = line.split('|')
    a, b = map(str.split, (a,b))
    a, b = digitize(a), digitize(b)

    p1 += (b.sum(1)[:,None] == np.array([2,4,3,7])).any(1).sum()

    for perm in map(np.array, it.permutations(range(7))):
        if (a[None,:,perm] == bins[:,None]).all(2).any(0).all():
            p2 += int("".join((b[None,:,perm] == bins[:,None]).all(2).argmax(0).astype(str)))
            break

print(p1)
print(p2)