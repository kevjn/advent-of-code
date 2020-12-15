#!/usr/bin/env python3.9
import itertools as it
import re
from collections import defaultdict

lines = [line.rstrip() for line in open('in1')]

mem = {}
i = 0

while i < len(lines):
    chunks = lines[i].split()
    mask = chunks[2] # 36 bits
    i += 1
    chunks = lines[i].split()
    while chunks[0] != 'mask':
        a = int(re.findall(r'\d+',chunks[0])[0])
        adr = f"{a:036b}"
        
        v = int(chunks[2])
        value = f"{v:036b}"

        results = ['']
        for j, bit in enumerate(mask):
            if bit == '0':
                for k in range(len(results)):
                    results[k] += adr[j]
            elif bit == '1':
                for k in range(len(results)):
                    results[k] += bit
            elif bit == 'X':
                for k in range(len(results.copy())):
                    results.append(results[k] + '1')
                    results[k] += '0'

            else: assert False

        for r in results:
            mem[int(r,2)] = v

        i += 1
        if i == len(lines): break
        chunks = lines[i].split()


_sum = sum(mem.values())
print(_sum)
