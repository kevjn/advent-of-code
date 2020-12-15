#!/usr/bin/env python3.9
import itertools as it

lines = open('in').read().split('\n\n')

any_sum = 0
every_sum = 0
for line in lines:
    l = line.split()

    any_sum += len(set.union(*[set(x) for x in l]))
    every_sum += len(set.intersection(*[set(x) for x in l]))
   
print(any_sum)
print(every_sum)