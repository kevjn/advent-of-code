#!/usr/bin/env python3.9

import numpy as np
import binascii
import itertools as it

line = open('input').readline().rstrip()

b = binascii.unhexlify(line)
b = iter(''.join(format(byte, '08b') for byte in b))

def take(x, n):
    try:
        return int("".join(it.islice(x, n)), 2)
    except:
        raise StopIteration

ops = {
    0: lambda args: np.sum(args),
    1: lambda args: np.prod(args),
    2: lambda args: np.min(args),
    3: lambda args: np.max(args),
    5: lambda args: np.greater(*args),
    6: lambda args: np.less(*args),
    7: lambda args: np.equal(*args),
}

V = 0
def parse():
    global V
    global b
    V += take(b, 3)
    T = take(b, 3)

    if T == 4: # literal value
        t = ''
        while True:
            c = next(b)
            t += "".join(it.islice(b, 4))
            if c == '0':
                return int(t,2)
            
    nums = []
    if next(b) == '0':
        L = take(b, 15)

        prev = b
        b = iter("".join(it.islice(b, L)))
        while True:
            try:
                n = parse()
            except StopIteration:
                break
            nums.append(n)
        b = prev

    else:
        L = take(b, 11)
        for _ in range(L):
            n = parse()
            nums.append(n)

    return ops[T](nums)

p2 = parse()
print(V)
print(p2)