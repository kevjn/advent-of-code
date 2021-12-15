#!/usr/bin/env python3.9

import numpy as np
import heapq

lines = np.array([list(line.rstrip()) for line in open('input')], dtype=int)

def dijkstra(lines, start, goal):
    cost = {start: 0}
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        g, (x, y) = heapq.heappop(pq)

        if (x,y) == goal:
            return g

        for dx,dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            n = (x + dx, y + dy)

            if set(n) & {-1, lines.shape[0]}: 
                continue

            new_cost = cost[(x,y)] + lines[n]
            if n not in cost or new_cost < cost[n]:
                cost[n] = new_cost
                p = new_cost
                heapq.heappush(pq, (p, n))

start = (0,0)
goal = (lines.shape[0]-1, lines.shape[1]-1)
print(dijkstra(lines, start, goal))

i = np.arange(5).repeat(lines.shape[0])
lines = np.tile(lines, (5,5))
lines += i
lines += i[:,None]
m = lines > 9
lines %= 10
lines[m] += 1

goal = (lines.shape[0]-1, lines.shape[1]-1)
print(dijkstra(lines, start, goal))