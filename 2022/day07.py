#!/usr/bin/env python3.10

import re
from collections import defaultdict

s = defaultdict(lambda: {'dirs': {}, 'files': {}})
d = []

cmds = open("input").read().split('$ ')

for cmd in cmds:
    if cmd.startswith('cd /'):
        d = ''

    elif cmd.startswith('cd ..'):
        d = "/".join(d.split('/')[:-1])

    elif cmd.startswith('cd '):
        d += '/' + re.findall(r"([A-z]+)", cmd)[-1]

    elif cmd.startswith('ls'):
        dirs = re.findall(r'dir ([A-z]+)', cmd)
        files = [int(x) for x in re.findall(r"\n([0-9]+)", cmd)]
        s[d]['dirs'] = dirs
        s[d]['files'] = files

def dir_size(cur_dir, dir, size=0):
    size += sum(dir['files'])
    for d in dir['dirs']:
        new_dir = cur_dir + '/' + d
        if new_dir not in s:
            raise Exception()
        size += dir_size(new_dir, s[new_dir], 0)
    return size

print(sum(sz for sz in [dir_size(*d, 0) for d in s.items()] if sz < 100000))

used = dir_size('', s[''], 0)
unused = 70000000 - used
min_size = 30000000 - unused

from itertools import starmap
print(min(sz for sz in starmap(dir_size, s.items()) if sz >= min_size))