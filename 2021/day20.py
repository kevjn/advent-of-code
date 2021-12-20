#!/usr/bin/env python3.9

import numpy as np

def printimg(img):
    print(np.array2string(img.astype(bool), formatter={'bool': {0: '.', 1: '#'}.get}))

alg, img = (line for line in open('input').read().rstrip().split('\n\n'))

alg = np.array([1 if x == '#' else 0 for x in alg])
img = np.array([[1 if x == '#' else 0 for x in y] for y in img.split('\n')])
img = np.pad(img, (100,100), mode='constant')

for step in range(50):
    ws = np.lib.stride_tricks.sliding_window_view(img, (3,3))
    w = ws.reshape(*ws.shape[:2],-1)
    i = (2**np.arange(3*3)[None,None,::-1] * w).sum(-1)
    img = alg[i]
    print(step+1, img.sum())