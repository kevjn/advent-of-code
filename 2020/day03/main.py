#!/usr/bin/env python3.9

import numpy as np
import math

pattern = [line.rstrip() for line in open('in1')]

print(\
    sum(pattern[i*1][(i*3)%len(pattern[0])] == '#' for i in range(len(pattern))))

print(\
    np.prod(\
        [sum(pattern[i*y][(i*x)%len(pattern[0])] == '#' for i in range(math.ceil(len(pattern)/y)))\
            for x,y in [(1,1), (3,1), (5,1), (7,1), (1,2)]]))