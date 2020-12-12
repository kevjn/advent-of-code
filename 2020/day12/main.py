#!/usr/bin/env python3.9
from math import pi, sin, cos, tan, atan, atan2
import re

lines = [line.rstrip() for line in open('in1')]

directions = {
    'E' : 0,
    'N' : pi/2,
    'W' : pi,
    'S' : 3 * pi/2
}

turn = {
    'L' : 1,
    'R' : -1
}

wx,wy = 10,1
x,y = 0,0

for line in lines:
    action, value = re.match(r'^([A-Z])(\d+)', line).groups()
    value = int(value)

    if action in directions:
        deg = directions[action]
        wx += cos(deg) * value
        wy += sin(deg) * value
        continue

    if action in turn:
        value = value * pi/180
        deg = atan2(wy,wx)
        deg += value * turn[action]

        amp = (wx**2 + wy**2)**(1/2)
        wx = cos(deg) * amp
        wy = sin(deg) * amp
        continue

    x += wx * value
    y += wy * value

print(abs(x) + abs(y))