#!/usr/bin/env python3.9

from common import ints
import numpy as np

cals = [sum(ints(cal)) for cal in open("input").read().split('\n\n')]

print(max(cals))

print(np.partition(cals, -3)[-3:].sum())