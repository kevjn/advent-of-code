#!/usr/bin/env python3.9

import numpy as np

lines = [list(int(x) for x in line.rstrip()) for line in open('input')]
bits = np.array(lines)

b = lambda x: int("".join(map(str, x.astype(int).tolist())), 2)

gamma = bits.sum(axis=0) > (bits.shape[0]/2)
gamma = b(gamma)

beta = bits.sum(axis=0) < (bits.shape[0]/2)
beta = b(beta)

ans = gamma * beta
print(ans)

oxy, co2 = bits.copy(), bits.copy()
for i in range(bits.shape[1]):
    if len(oxy) > 1:
        oxy = oxy[oxy[:,i] == (oxy[:,i].sum() >= len(oxy[:,i])/2)]
    if len(co2) > 1:
        co2 = co2[co2[:,i] == (co2[:,i].sum() < len(co2[:,i])/2)]

ans = b(oxy[0]) * b(co2[0])
print(ans)