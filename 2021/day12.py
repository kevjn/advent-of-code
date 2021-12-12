#!/usr/bin/env python3.9

from collections import defaultdict

lines = [line.rstrip() for line in open('input')]
m = defaultdict(list)

for line in lines:
    a,b = line.split('-')
    m[a].append(b)
    m[b].append(a)

q = [('start', {'start'}, None)]

p1, p2 = 0,0
while q:
    a, seen, exclude = q.pop()

    for b in filter(lambda x: x != 'start', m[a]):
        if b == 'end':
            p1 += exclude is None
            p2 += 1
            continue

        if b not in seen:
            q.append((b, seen | [set(), set([b])][b.islower()], exclude))
        elif b in seen and exclude is None:
            q.append((b, seen, b))

print(p1)
print(p2)