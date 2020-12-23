#!/usr/bin/env python
import itertools as it

cups = [int(cup) for cup in open('input').read().rstrip()]

for _ in range(100):
    cur = cups[0]
    picks = cups[1:4]
    del cups[0:4]

    dest = cur-1
    while dest not in cups:
        dest -= 1
        if dest < min(cups):
            dest = max(cups)

    dest_idx = cups.index(dest)
    cups = cups[:dest_idx+1] + picks + cups[dest_idx+1:] + [cur]

n = cups.index(1)
cups = cups[n:] + cups[:n]

print("".join(str(cup) for cup in cups[1:]))