#!/usr/bin/env python3.9

import numpy as np

lines = [line.rstrip() for line in open('input')]

x,y = 0,0

for line in lines:
    cmd, i = line.split()
    i = int(i)

    if cmd == "forward": 
        x += i
        continue

    y += [1, -1][cmd == "up"] * i

ans = x*y
print(ans)

x,y = 0,0
aim = 0

for line in lines:
    cmd, i = line.split()
    i = int(i)

    if cmd == "forward": 
        x += i
        y += aim * i
        continue

    aim += [1, -1][cmd == "up"] * i

ans = x*y
print(ans)