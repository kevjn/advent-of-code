import re
import numpy as np

directions = {
    'R': (1,0),
    '0': (1,0),

    'L': (-1,0),
    '2': (-1,0),

    'U': (0,-1),
    '3': (0,-1),

    'D': (0,1),
    '1': (0,1),
}

corners_p1 = [(0,0)]
corners_p2 = [(0,0)]

for line in open("input"):
    direction,n,hx = re.match(r"([A-Z]) (\d+) \(#(.+)\)",line).groups()

    dx,dy = directions[direction]
    length = int(n)
    cx,cy = corners_p1[-1]
    corners_p1.append((cx + dx*length,cy + dy*length))

    dx,dy = directions[hx[-1]]
    length = int(hx[:-1],16)
    cx,cy = corners_p2[-1]
    corners_p2.append((cx + dx*length,cy + dy*length))

for corners in [corners_p1,corners_p2]:
    x,y = np.stack(corners).T
    i=np.r_[:len(x)]
    area=np.abs((x[i-1]*y[i]-x[i]*y[i-1]).sum()//2) 
    ans = area + ((np.abs(np.diff(x)).sum() + np.abs(np.diff(y)).sum()) // 2) + 1
    print(ans)
