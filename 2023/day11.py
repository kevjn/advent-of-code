import numpy as np, itertools as it

image = np.array([[1 if c == '#' else 0 for c in line.rstrip()] for line in open("input")])
galaxies = np.nonzero(image)

expanding_cols = (image==0).all(axis=0)
expanding_rows = (image==0).all(axis=1)

image = np.zeros_like(image)
image[expanding_rows] = 1
image[:,expanding_cols] = 1

galaxies = np.stack(galaxies, axis=1)

p1 = 0
p2 = 0
for (sx,sy),(gx,gy) in it.combinations(galaxies,2):
    ms,me = min(sy,gy), max(sy, gy)
    x = image[:,ms:me][sx]
    y = image[sx:gx][:,gy]
    p1 += int((sum(x*(2-1) + 1) + sum(y*(2-1) + 1)))
    p2 += int((sum(x*(1e6-1) + 1) + sum(y*(1e6-1) + 1)))

print(p1)
print(p2)