#!/usr/bin/env python
import itertools as it

cups = [int(cup) for cup in open('input').read().rstrip()]

cups += range(max(cups)+1, int(1e6)+1)

cur = cups[0]
cups = {cup : nxt for cup, nxt in zip(cups, cups[1:] + [cups[0]])}
for _ in range(int(1e7)):
    start = cups[cur]
    mid = cups[cups[cur]]
    end = cups[cups[cups[cur]]]

    remove = {start, mid, end}
    dest = cur - 1 if cur > 1 else int(1e6)
    while dest in remove:
        dest = dest-1 if dest != 1 else int(1e6)
    
    cups[cur] = cups[end]
    cups[end] = cups[dest]
    cups[dest] = start
    cur = cups[cur]

a,b = cups[1], cups[cups[1]]
print(a * b)