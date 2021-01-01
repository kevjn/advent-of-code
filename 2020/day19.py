#!/usr/bin/env python
import itertools as it
import re

rule_lines, message_lines = open('input').read().split('\n\n')

rules = {}
regex = r'(\d+): (?:([\d ]+)(?:\| ([\d ]+)|)|\"([a-z])\")'

for line in rule_lines.split('\n'):
    key, subrule1, subrule2, ch = re.match(regex, line).groups()
    assert key
    key = int(key)

    if ch:
        rules[key] = ch
        continue

    rules[key] = [tuple(map(int,subrule1.split()))]

    if subrule2:
        rules[key].append(tuple(map(int,subrule2.split())))

rules[8] = [tuple([42] * n) for n in range(1,10)]
rules[11] = [tuple([42] * n + [31] * n) for n in range(1,5)]

def expand(rn):
    subrules = rules[rn]
    return '(' + '|'.join("".join(expand(rule) if isinstance(rules[rule],list) else rules[rule] for rule in s) for s in subrules) + ')'

regex = '^' + expand(0) + '$'

ans = 0
for line in message_lines.split('\n'):
    if re.match(regex, line):
        ans += 1

print(ans)