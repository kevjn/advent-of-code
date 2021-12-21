#!/usr/bin/env python3.9

import numpy as np
import re
import itertools as it

_, player1, _, player2 = map(int,re.findall(r'(\d+)', open('input').read()))

dice = np.tile(np.arange(1,101), 15).reshape(-1,3)
dice = dice.sum(-1)

a,b = player1, player2
atot = 0
btot = 0

for i,(da,db) in enumerate(zip(dice[::2], dice[1::2])):
    a = ((a - 1) + da) % 10 + 1
    atot += a
    if atot >= 1000:
        ans = (i*3*2 + 3) * btot
        break

    b = ((b - 1) + db) % 10 + 1
    btot += b
    if btot >= 1000:
        ans = (i*3*2 + 3) * atot
        break

print(ans)

DP = {}
dice = np.array(list(it.product([1,2,3], [1,2,3], [1,2,3])))
dice = dice.sum(-1)

def f(*key):
    a, b, atot, btot = key
    if atot >= 21:
        return 1,0

    if btot >= 21:
        return 0,1

    if key in DP:
        return DP[key]

    wa, wb = 0,0
    for d in dice:
        an = ((a - 1) + d) % 10 + 1
        x,y = f(b, an, btot, an + atot)
        wa += y
        wb += x

    DP[key] = wa, wb
    return wa, wb

a,b = player1, player2
print(max(f(a, b, 0, 0)))