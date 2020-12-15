#!/usr/bin/env python3.9

from collections import defaultdict
import itertools as it
from re import split

lines = [line.strip() for line in open('in1')] + ['']

i = 0
part1 = 0
part2 = 0
while i < len(lines):
    b = lines[i:].index('')
    l = lines[i:i+b]
    i += b
    i += 1

    l = ' '.join(l)
    l = split(' |:', l)

    valid = len(l) == 16 - ('cid' not in l )*2
    if not valid: 
        continue
    part1 += 1

    d = {l[i]:l[i+1] for i in range(0,len(l),2)}

    valid = len(d['byr']) == 4 and 1920 <= int(d['byr']) <= 2002 and \
        len(d['iyr']) == 4 and 2010 <= int(d['iyr']) <= 2020 and \
        len(d['eyr']) == 4 and 2020 <= int(d['eyr']) <= 2030 and \
        ((d['hgt'][-2:] == 'cm' and 150 <= int(d['hgt'][:-2]) <= 193) or \
        (d['hgt'][-2:] == 'in' and 59 <= int(d['hgt'][:-2]) <= 76)) and \
        d['hcl'][0] == '#' and len(d['hcl'][1:]) == 6 and \
        set(list(d['hcl'][1:])).issubset([str(x) for x in range(10)] + [chr(i) for i in range(ord('a'), ord('f')+1)]) and \
        d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
        len(str(d['pid'])) == 9
    
    part2 += valid

print(part1)
print(part2)
