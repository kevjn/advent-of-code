import numpy as np
import itertools as it

mirror = {
    '\\': lambda x,y,dx,dy: [(x,y,dy,dx)],
    '/': lambda x,y,dx,dy: [(x,y,dy*-1,dx*-1)],
    '|': lambda x,y,dx,dy: [(x,y,0,1),[x,y,0,-1]] if dy == 0 else [(x,y,dx,dy)],
    '-': lambda x,y,dx,dy: [(x,y,1,0),[x,y,-1,0]] if dx == 0 else [(x,y,dx,dy)],
    '.': lambda x,y,dx,dy: [(x,y,dx,dy)]
}

mirrors =  {}

for yy,line in enumerate(open("input")):
    for xx,char in enumerate(line.rstrip()):
        if char in mirror:
            mirrors[(xx,yy)] = mirror[char]

def search(space):
   for (sx,sy),(dirx,diry) in space:
        start = sx,sy,dirx,diry

        seen = {start}
        beams = [start]

        while beams:
            new_beams = []
            for (x,y,dx,dy) in beams:
                paths = mirrors[(x,y)](x,y,dx,dy)
                for (x,y,dx,dy) in paths:
                    if x+dx in range(xx+1) and y+dy in range(yy+1):
                        new_beams.append((x+dx,y+dy,dx,dy))

            beams = [beam for beam in new_beams if beam not in seen]
            seen |= set(beams)

        seen = {(x,y) for x,y,dx,dy in seen}
        yield len(seen)

print(next(search([((0,0),(1,0))])))
print(max(search(it.product(zip(range(xx),it.repeat(0)),((0,1),(0,-1))))))