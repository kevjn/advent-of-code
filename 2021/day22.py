#!/usr/bin/env python3.9

import numpy as np
import re
from collections import defaultdict

lines = [(line.startswith('on'), *(map(int,re.findall(r'-?\d+', line)))) for line in open('input').read().split('\n')]

status = defaultdict(int)
volume = {}

for on, *xyz in lines:
    xyz = np.array(xyz)

    for box, value in status.copy().items():
        # top-left and bottom-right
        tl = np.maximum(xyz[::2], box[::2])
        br = np.minimum(xyz[1::2], box[1::2])

        if (tl <= br).all():
            # intersection found
            key = tuple(np.vstack((tl,br)).ravel('F'))
            status[key] -= value
            volume[key] = np.prod(br - tl + 1)
    
    status[tuple(xyz)] += on
    volume[tuple(xyz)] = np.prod(xyz[1::2] - xyz[::2] + 1)

p1 = sum(v * status[k] for k,v in volume.items() if (np.less_equal(k, 50) & np.greater_equal(k, -50)).all())
print(p1)

p2 = sum(v * status[k] for k,v in volume.items())
print(p2)