import numpy as np

sequences = np.array([[*map(int,line.split())] for line in open("input")])

p1,p2 = 0,0
for seq in sequences:
    c = seq
    history = [c]
    while not (c == 0).all():
        c = np.diff(c)
        history.append(c)
    hr = history[::-1]
    dx,dy = 0,0
    for h in hr:
        dx = h[-1]+dx
        dy = h[0]-dy
    p1 += dx
    p2 += dy

print(p1)
print(p2)