#!/usr/bin/env python3.10

import numpy as np
import re
import copy

_monkeys = []

for m in open("input").read().split('\n\n'):
    _, start, op, test, true, false, *_ = m.split('\n')

    _monkeys.append({
        'items': list(map(int,re.findall(r'\d+', start))),
        'op': op.split(': new = ')[1],
        'div': int(next(iter(re.findall(r'\d+', test)))),
        True: int(next(iter(re.findall(r'\d+', true)))),
        False: int(next(iter(re.findall(r'\d+', false)))),
        'i': 0
    })

p = np.prod([m['div'] for m in _monkeys])

for p1 in (True, False):
    monkeys = copy.deepcopy(_monkeys)
    for _ in range(20 if p1 else 10_000):
        for monkey in monkeys:
            for item in monkey['items']:
                monkey['i'] += 1
                w = eval(monkey['op'], {'old': item})
                if p1:
                    w //= 3
                else:
                    w %= p
                other = monkeys[monkey[w % monkey['div'] == 0]]
                other['items'].append(w)

            monkey['items'].clear()

    *_, a,b = sorted([m['i'] for m in monkeys])
    print(a*b)