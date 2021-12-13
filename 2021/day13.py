#!/usr/bin/env python3.9

from collections import defaultdict
import numpy as np

dots, folds = open('input').read().split('\n\n')
dots = np.array([[*map(int, x.split(','))] for x in dots.split('\n')])

paper = np.zeros((dots[:,0].max()+1, dots[:,1].max()+1), dtype=int)
for dot in dots:
    paper[tuple(dot)] = 1

paper = paper.T

def fold():
    global paper
    for fold in folds.split('\n'):
        xy, n = fold.split()[-1].split('=')
        n = int(n)
        if xy == 'x':
            a,b = paper[:,:n], paper[:,n+1:]
            paper = a | b[:,::-1]
            yield paper
        if xy == 'y':
            a,b = paper[:n], paper[n+1:]
            paper = a | b[::-1]
            yield paper

fold = fold()
paper = next(fold)
print(paper.sum())

paper = list(fold)[-1]
np.set_printoptions(linewidth=200)
print(paper)