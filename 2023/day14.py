import numpy as np
import itertools as it

trs = str.maketrans({'.': '0', '#': '1', 'O': '2'})
arr = np.array([[int(c.translate(trs)) for c in line.rstrip()] for line in open("input")])
arr = np.rot90(arr,-1)

def score(arr):
    return ((arr == 2).sum(axis=0) * (np.r_[:arr.shape[0]]+1)).sum()

def move_rocks(arr):
    arr = arr.copy()
    while True:
        windows = np.lib.stride_tricks.sliding_window_view(arr,(1,2),writeable=True)
        m = (windows == np.array([2,0])).all(axis=-1)
        if not m.any():
            break
        windows[m] = np.array([0,2])
    return arr

print(score(move_rocks(arr)))

memo = {}
n = int(1e9)
for memo_size in range(n):
    key = hash(arr.data.tobytes())
    if key in memo:
        break

    for r in range(4):
        arr = move_rocks(arr)
        arr = np.rot90(arr,-1)

    memo[key] = arr.copy()

start = arr.copy()
for period in range(1,n):
    key = hash(arr.data.tobytes())
    arr = memo[key].copy()
    if (arr == start).all():
        break

N = (n-memo_size)%period
for _ in range(N):
    key = hash(arr.data.tobytes())
    arr = memo[key].copy()

print(score(arr))