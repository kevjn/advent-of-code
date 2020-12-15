#!/usr/bin/env python3.9

lines = [line.strip() for line in open('in1')]

ans = [-1] * 843 * 2

for line in lines:

    a = [s/2 for s in [2**x for x in range(7,0,-1)]]
    r = sum(d for i,d in enumerate(a) if line[i] == 'B')

    b = [s/2 for s in [2**x for x in range(3,0,-1)]]
    c = sum(d for i,d in enumerate(b) if line[i+7] == 'R')

    _id = r*8 +c
    ans[int(_id)] = int(_id)

_max = max(ans)
print(_max)

mia = -1

for i in range(0, max(ans)):
    if ans[i-1] != -1 and ans[i+1] != -1 and ans[i] == -1:
        mia = i

print(mia)
