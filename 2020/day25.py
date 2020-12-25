#!/usr/bin/env python
card, door = [int(line.rstrip()) for line in open('input')]

def transform(loop_size, subject_num):
    n = 1
    for _ in range(loop_size):
        n *= subject_num
        n = n % 20201227
    return n

loop_size_card = None
loop_size_door = None

n = 1
loop_size = 1
while not loop_size_card or not loop_size_door:
    n *= 7
    n = n % 20201227
    if n == card:
        loop_size_card = loop_size
    if n == door:
        loop_size_door = loop_size
    
    loop_size += 1

ek = transform(loop_size_card, door)
assert ek == transform(loop_size_door, card)
print(ek)