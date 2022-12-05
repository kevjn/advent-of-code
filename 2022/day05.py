#!/usr/bin/env python3.10

from common import ints
import re

for p1 in (True, False):
    stacks, instructions = open("input").read().split('\n\n')
    stacks = [[]] + [re.findall(r'[A-z]', ''.join(x[::-1])) for x in zip(*stacks.split('\n')) if x[-1].isdigit()]

    for instr in instructions.rstrip().split('\n'):
        n, fr, to = ints(instr)
        a,b = stacks[fr][-n:], stacks[fr][:-n]
        stacks[to].extend(a[::-1] if p1 else a)
        stacks[fr] = b

    print("".join(stack[-1] if stack else '' for stack in stacks))