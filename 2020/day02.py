#!/usr/bin/env python3.9

lines = [line.strip().replace(': ', ' ').split() for line in open('input')]

# Part 1

valid = 0
for line in lines:
    r = line[0].split('-')
    p1 = int(r[0])
    p2 = int(r[1])
    char = line[1]
    pwd = line[2]

    if p1 <= pwd.count(char) <= p2:
        valid += 1

print(valid)

# Part 2

valid = 0
for line in lines:
    r = line[0].split('-')
    p1 = int(r[0]) - 1
    p2 = int(r[1]) - 1
    char = line[1]
    pwd = line[2]

    if (pwd[p1] == char) ^ (pwd[p2] == char):
        valid += 1

print(valid)
