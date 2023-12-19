import numpy as np 
from collections import defaultdict

arr = np.array([[int(d) for d in line.rstrip()] for line in open("input")]).T

start = (0,0,1,0,0)
goal = tuple(np.array(arr.shape)-1)

def directions_p1(dx,dy,length):
    if length < 3:
        yield dx,dy,length+1
    yield dy,dx,1
    yield dy*-1,dx*-1,1

def directions_p2(dx,dy,length):
    if length < 10:
        yield dx,dy,length+1
    if length > 3:
        yield dy,dx,1
        yield dy*-1,dx*-1,1

def search(dir_fn):
    cost = {start: 0}
    queue = [start]

    while queue:
        x,y,dx,dy,length = queue.pop(0)
        for ndx,ndy,nlength in dir_fn(dx,dy,length):
            nxt = x+ndx,y+ndy,ndx,ndy,nlength
            if x+ndx < 0 or y+ndy < 0:
                continue
            nxt_coord = nxt[0],nxt[1]
            try:
                new_cost = cost[(x,y,dx,dy,length)] + arr[nxt_coord]
            except IndexError:
                continue
            if nxt not in cost:
                cost[nxt] = new_cost
                queue.append(nxt)
            elif new_cost < cost[nxt]:
                cost[nxt] = new_cost
                queue.append(nxt)
    return cost

p1_cost = search(directions_p1)
print(min(v for (x,y,*_,l),v in p1_cost.items() if (x,y) == goal))

p2_cost = search(directions_p2)
print(min(v for (x,y,*_,l),v in p2_cost.items() if (x,y) == goal and l > 3))