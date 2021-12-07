#!/usr/bin/env python3.9

import numpy as np

n = np.loadtxt(open("input").readline().split(','), int)

i = np.arange(n.max()).repeat(len(n)).reshape(n.max(),-1)

a = np.abs(i - n)
ans = a.sum(1).min()
print(ans)

ans = (a*(a+1)//2).sum(1).min()
print(ans)