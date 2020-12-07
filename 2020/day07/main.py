#!/usr/bin/env python3.9
import itertools as it
import re
from collections import defaultdict

def expand_pt1(bags, key):
    ret = []
    for c in bags[key]:
        ret += [c[1]] + expand_pt1(bags, c[1])
    return ret

def expand_pt2(bags, key, acc):
    for c in bags[key]:
        acc[key] += c[0] + c[0] * expand_pt2(bags, c[1], acc.copy())
    return acc[key]

lines = [line.rstrip() for line in open('in1')]

bags = defaultdict(list)

for line in lines:
    key = re.search('^(\w+ \w+)', line).group()
    contents = [(int(x),y) for x,y in re.findall(r"(\d+) (\w+ \w+)", line)]

    bags[key] = contents

ans = 0
for key in bags:
    if 'shiny gold' in expand_pt1(bags, key):
        ans += 1

print(ans)

acc = defaultdict(int)

expand_pt2(bags, 'shiny gold', acc)

print(acc['shiny gold'])