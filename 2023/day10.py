from collections import defaultdict
import numpy as np

pipes = {
    '|': ((-1,0), (1,0)),
    '-': ((0,-1), (0,1)),
    'L': ((-1,0), (0,1)), 
    'J': ((-1,0), (0,-1)),
    '7': ((0,-1), (1,0)), 
    'F': ((1,0), (0,1))
}

network = defaultdict(lambda: [])
start = None
for row,line in enumerate(open("input")):
    for col,char in enumerate(line.rstrip()):
        if char in pipes:
            (a,b),(c,d) = pipes[char]
            network[(row+a,col+b)] += [(row,col)]
            network[(row+c,col+d)] += [(row,col)]
        if char == 'S':
            start = (row,col)

queue = [start]
costs = {start: 0}

while queue:
    cur = queue.pop(0)
    for nxt in network[cur]:
        if nxt not in costs:
            costs[nxt] = costs[cur]+1
            queue.append(nxt)

print(max(costs.values()))

arr = np.array([[ord(c) for c in line.rstrip()] for line in open("input")])
upscale = {
    ord('.'): np.array([[0,0,0],[0,0,0],[0,0,0]]),
    ord('S'): np.array([[0,1,0],[1,1,1],[0,1,0]]),
    ord('|'): np.array([[0,1,0],[0,1,0],[0,1,0]]),
    ord('-'): np.array([[0,0,0],[1,1,1],[0,0,0]]),
    ord('L'): np.array([[0,1,0],[0,1,1],[0,0,0]]),
    ord('J'): np.array([[0,1,0],[1,1,0],[0,0,0]]),
    ord('7'): np.array([[0,0,0],[1,1,0],[0,1,0]]),
    ord('F'): np.array([[0,0,0],[0,1,1],[0,1,0]]),
}

n = 3
maze = np.full(np.array(arr.shape)*n+2,9).astype(int)
windows = np.lib.stride_tricks.sliding_window_view(maze, (n,n), writeable=True)[1:-1:n,1:-1:n]
for r in range(arr.shape[0]):
    for c in range(arr.shape[1]):
        windows[r,c] = upscale[arr[r,c]]

# flood-fill
start = (1,1)
maze[*start] = 2
queue = [start]
while queue:
    (r,c) = queue.pop(0)
    for dx,dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nxt = r+dx,c+dy
        if maze[nxt] in [1,2,9]:
            continue
        maze[nxt] = 2
        queue.append(nxt)

ans = 0
for r in range(arr.shape[0]):
    for c in range(arr.shape[1]):
        ans += (windows[r,c] == 0).sum() > 5

print(ans)