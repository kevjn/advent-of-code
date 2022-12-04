#!/usr/bin/env python3.10

from common import positive_ints

lines = [positive_ints(line) for line in open("input")]

print(sum((a <= x and b >= y) or (x <= a and y >= b) for (a,b,x,y) in lines))

print(sum((len(set(range(a,b+1)) & set(range(x,y+1))) > 0) for (a,b,x,y) in lines))