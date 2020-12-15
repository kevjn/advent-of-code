#!/usr/bin/env python3.9

from itertools import combinations

entries = [int(line.strip()) for line in open('input')]

for a,b,c in combinations(entries, 3):
    if a + b == 2020: print("part one: ", a*b)
    if a + b + c == 2020: print("part two: ", a*b*c)
