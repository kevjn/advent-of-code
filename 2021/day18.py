#!/usr/bin/env python3.9

import itertools as it
import numpy as np
from collections.abc import Iterable

def flatten(items, i=0):
    for x in items:
        if isinstance(x, Iterable):
            yield from flatten(x,i+1)
        else:
            yield i, x

def explode(n):
    # n = n.copy()
    for i,j in zip(range(len(n)-1), range(1,len(n))):
        if n[i][0] == n[j][0] == 4:
            break
    else:
        return n
    
    if i > 0:
        n[i-1] = (n[i-1][0], n[i-1][1] + n[i][1])

    if j < len(n)-1:
        n[j+1] = (n[j+1][0], n[j+1][1] + n[j][1])

    del n[i:j+1]

    return n[:i] + [(3,0)] + n[i:]

def split(n):
    for i,x in enumerate(n):
        if x[1] > 9:
            break
    else:
        return n

    l,r = x[1]//2, (x[1]+1)//2
    return n[:i] + [(x[0]+1,l), (x[0]+1,r)] + n[i+1:]

def magnitude(n):
    while not all(x[0] == 0 for x in n):
        a = np.array(n)[:,0]
        i = list(np.where(a == a.max())[0])
        r = []
        j = -1
        while (j := j + 1) < len(n):
            if len(i) == 0:
                r.append(n[j])

            elif len(i) > 1 and j == i[0] and j+1 == i[1]:
                # reduce pair
                l = n[j][0]-1
                r.append((l, 3*n[j][1] + 2*n[j+1][1]))
                del i[:2]
                j += 1

            elif len(i) == 1 and j == i[0]:
                l = n[j][0]-1
                r.append((l, n[j][1]))
                continue
                
            else:
                r.append(n[j])
        
        n = r

    assert len(n) == 2
    return n[0][1] * 3 + n[1][1] * 2

def red(x):
    while True:
        n = explode(x)
        if n == x:
            n = split(x)
            if n == x: 
                break
        x = n

    return n

def add(x,y):
    r = x + y
    return [(rr[0]+1, rr[1]) for rr in r]

lines = [eval(line.rstrip()) for line in open('input')]
lines = [list(flatten(line)) for line in lines]

x,y = lines[0], lines[1]
x = add(x,y)
x = red(x)

for y in lines[2:]:
    x = add(x,y)
    x = red(x)

p1 = magnitude(x)
print(p1)

p2 = 0
for i,j in it.product(range(len(lines)), range(len(lines))):
    if i == j:
        continue
    x = magnitude(red(add(lines[i], lines[j])))
    y = magnitude(red(add(lines[j], lines[i])))
    p2 = max(max(x,y), p2)
    
print(p2)