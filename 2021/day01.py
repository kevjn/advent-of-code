#!/usr/bin/env python3.9
import numpy as np

lines = [int(line.rstrip()) for line in open('input')]
lines = np.array(lines)

ans = (np.diff(lines) > 0).sum()
print(ans)

windows = np.lib.stride_tricks.sliding_window_view(lines, (3))
ans = (np.diff(windows.sum(axis=1)) > 0).sum()
print(ans)