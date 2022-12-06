#!/usr/bin/env python3.10

import numpy as np

markers = np.array([ord(m) for m in open("input").read().rstrip()])

for n in (4,14):
    windows = np.lib.stride_tricks.sliding_window_view(markers, (n,))
    for i, w in enumerate(windows):
        if len(set(w)) == n:
            print(i+n)
            break