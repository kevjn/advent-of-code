import re, numpy as np, itertools as it, math

symbols = set(re.findall(r'[^0-9,.\n]', open("input").read()))
mapping = str.maketrans({k: '-1' for k in symbols} | {'.': '-2'})
sch = np.array([list(int(c.translate(mapping)) for c in line.rstrip()) for line in open("input")])

m = np.pad(sch.copy(), 1)
ws = np.lib.stride_tricks.sliding_window_view(m, (3,3), writeable=True)
ws[ws[:,:,1,1] == -1] = -1
m = m[1:-1,1:-1]
mask = (m == -1).astype(int)

ans = 0
for line, m in zip(sch, mask):
    a = ''
    include = False
    for i,digit in enumerate(line):
        if digit in [-1,-2]:
            if include:
                ans += int(a)
            a = ''
            include = False
            continue
        if m[i] == 1:
            include = True
        a += str(digit)
print(ans)

symbols = set(re.findall(r'[^0-9,.\n]', open("input").read()))
mapping = str.maketrans({k: '-1' for k in symbols} | {'.': '-2', '*': '-3'})
schema = np.array([list(int(c.translate(mapping)) for c in line.rstrip()) for line in open("input")])

from collections import defaultdict

height, width = schema.shape

indices = schema.copy()
index = 0
i_map = defaultdict(lambda: '', {})
for r in range(height):
    index += 1
    for c in range(width):
        if schema[r,c] >= 0:
            indices[r,c] = index
            i_map[index] = i_map[index] + str(schema[r,c])
        else:
            index += 1

ws = np.lib.stride_tricks.sliding_window_view(np.pad(indices, 1), (3,3), writeable=True)
ans = 0
for r,c in it.product(range(height), range(width)):
    window = ws[r,c]
    if window[1,1] == -3:
        s = set(window[window > 0])
        if len(s) == 2:
            a,b = s
            ans += int(i_map[a]) * int(i_map[b])
print(ans)