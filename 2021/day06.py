#!/usr/bin/env python3.9

import numpy as np

n = np.loadtxt(open("input").readline().split(','), int)

fish = np.bincount(n, minlength=9)
for day in range(80):
    fish = np.roll(fish, -1)
    fish[6] += fish[-1]

print(fish.sum())

for day in range(256-80):
    fish = np.roll(fish, -1)
    fish[6] += fish[-1]

print(fish.sum())