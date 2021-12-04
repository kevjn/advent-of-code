#!/usr/bin/env python3.9

import numpy as np

lines = [line.rstrip() for line in open('input')]

numbers = [int(x) for x in lines[0].split(',')]

bingo = []
for line in lines[1:]:
    if line == '':
        bingo.append([])
        continue
    bingo[-1].append([int(x) for x in line.split()])

bingo = np.array(bingo)
marked = np.zeros_like(bingo).astype(bool)

for n in numbers:
    marked[np.where(bingo == n)] = True

    # rows
    if marked.all(axis=-1).any():
        i = np.where(marked.all(axis=-1))[0]
        break

    # columns
    if marked.transpose(0,2,1).all(axis=-1).any():
        i = np.where(marked.transpose(0,2,1).all(axis=-1))[0]
        break


ans = bingo[i][~marked[i]].sum() * n
print(ans)

winners = set()
for n in numbers:
    marked[np.where(bingo == n)] = True

    if (marked.all(axis=-1).any(axis=1) | marked.transpose(0,2,1).all(axis=-1).any(axis=1)).all():
        last = (set(range(len(bingo))) - winners).pop()
        break

    if marked.all(axis=-1).any():
        i = np.where(marked.all(axis=-1))[0]
        winners = winners.union(set(i))

    if marked.transpose(0,2,1).all(axis=-1).any():
        i = np.where(marked.transpose(0,2,1).all(axis=-1))[0]
        winners = winners.union(set(i))

ans = bingo[last][~marked[last]].sum() * n
print(ans)