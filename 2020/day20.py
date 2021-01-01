#!/usr/bin/env python
import regex as re
from collections import defaultdict
from math import prod

class Tile:
    edge_cnt = defaultdict(int)
    edge_to_tile = defaultdict(set)

    def __init__(self, nr, content):
        self.nr = nr
        self.edges = content[0], content[-1], ''.join(x[0] for x in content), ''.join(x[-1] for x in content)
        self.NORTH, self.SOUTH, self.WEST, self.EAST = self.edges

        self.edges = [min(e, e[::-1]) for e in self.edges]
        self.content = content

    def flip(self):
        self.content = '\n'.join(x[::-1] for x in self.content).split('\n')
        self.__init__(self.nr, self.content)

    def rot(self):
        self.content = ["".join(x[::-1]) for x in zip(*self.content)]
        self.__init__(self.nr, self.content)

    @property
    def is_corner(self):
        return sum(self.edge_cnt[edge] == 1 for edge in self.edges) == 2
    
    @property
    def is_top_left(self):
        return Tile.edge_cnt[self.edges[0]] == 1 and Tile.edge_cnt[self.edges[2]] == 1

    def orientations(self):
        for _ in range(4):
            yield self.flip()
            self.flip()
            yield self.rot()

tiles = {}

for tile in open('input').read().rstrip().split('\n\n'):
    head, body = tile.split('\n', 1)
    tile_nr = int(re.search(r'(\d+)', head).group(0))
    tiles[tile_nr] = Tile(tile_nr, body.split('\n'))

    for e in tiles[tile_nr].edges:
        Tile.edge_cnt[e] += 1
        Tile.edge_to_tile[e].add(tile_nr)

corners = [t for t in tiles.values() if t.is_corner]
print(prod(t.nr for t in corners))

# top-left corner
corner = next(tile for tile in corners for _ in tile.orientations() if tile.is_top_left)

used = set([corner.nr])
image = [[corner.nr]]
tile = corner

edge = tile.edges[3]
while _next := next((tiles[nr] for nr in Tile.edge_to_tile[edge] if nr not in used), None):
    for _ in _next.orientations():
        if _next.WEST == tile.EAST:
            break
    used.add(_next.nr)
    tile = _next
    edge = _next.edges[3]
    image[0] += [_next.nr]

while len(used) < len(tiles):
    row = []
    for nr in image[-1]:
        tile = tiles[nr]
        edge = tile.edges[1]
        _next = next(tiles[nr] for nr in Tile.edge_to_tile[edge] if nr not in used)
        for _ in _next.orientations():
            if _next.NORTH == tile.SOUTH:
                break 
        row += [_next.nr]
        used.add(_next.nr)
    image.append(row)

def crop(content):
    return [col[1:-1] for col in content[1:-1]]

img = []
for nr in image:
    r = list(map(lambda nr: crop(tiles[nr].content), nr))
    img += ["".join(x) for x in zip(*r)]

w = len(img[0])
big = Tile(0, img)
for _ in big.orientations():
    line = "".join(i for i in big.content)
    m = re.findall(rf'#.{{{w-19}}}#.{{4}}##.{{4}}##.{{4}}###.{{{w-19}}}#.{{2}}#.{{2}}#.{{2}}#.{{2}}#.{{2}}#.{{5}}', line, overlapped=True)
    if m: break

print(line.count('#') - len(m) * 15)