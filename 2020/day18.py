#!/usr/bin/env python3.9
import itertools as it
from collections import defaultdict
import re
import numpy as np
from operator import add, mul

lines = [line.rstrip() for line in open('input')]

def eval_pt1(line):
    a,b = 'x','x'
    ans = 0
    op = add
    i = -1
    while (i := i + 1) < len(line):
        ch = line[i]

        if ch == ')':
            return ans

        if ch == '(':
            skip = 0
            n = 1
            for j in range(i+1,len(line)):
                _ch = line[j]
                if _ch == '(':
                    skip += 1
                    continue
                if _ch == ')':
                    if skip > 0:
                        skip -= 1
                        continue
                    n = j
                    break
            
            _line = line[i+1:n]
            if a == 'x':
                a = eval_pt1(_line)
            else:
                ans = op(a,eval_pt1(_line))
                a,b = ans, 'x'

            i = n

        elif ch == '*':
            op = mul
        
        elif ch == '+':
            op = add

        elif ch.isdigit() and a == 'x':
            a = int(ch)
        
        elif ch.isdigit():
            b = int(ch)
            ans = op(a,b)
            a,b = ans,'x'

    return ans

def eval_pt2(line):
    class custom_int:
        def __init__(self, v):
            self.v = v
        def __add__(self, other):
            return custom_int(self.v * other.v)
        def __mul__(self, other):
            return custom_int(self.v + other.v)


    line = line.replace('+','{0}').replace('*','{1}').format('*','+')
    line = re.sub(r'(\d)', r'custom_int(\1)', line)
        
    return eval(line).v


ans = 0
for line in lines:
    ans += eval_pt1(line)

print(ans)

ans = 0
for line in lines:
    ans += eval_pt2(line)

print(ans)
