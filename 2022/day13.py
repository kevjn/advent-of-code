#!/usr/bin/env python3.10

packets = [x for x in open("input").read().split("\n\n")]

def compare(a,b):
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return 0
        if a > b:
            return 1
        return -1

    if isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    
    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b)

    if isinstance(a, list) and isinstance(b, list):
        for left,right in zip(a,b):
            if (n := compare(left, right)) != 0:
                return n
            
        if len(a) == len(b):
            return 0
        
        if len(a) > len(b):
            return 1

        return -1

ans = 0
for i, pkt in enumerate(packets, 1):
    a,b = map(eval, pkt.split())
    if compare(a,b) == -1:
        ans += i
print(ans)

import functools
packets.append("[[2]]\n[[6]]")
packets = sum([x.split() for x in packets], [])
packets = [eval(x) for x in packets]
sorted_packets = sorted(packets, key=functools.cmp_to_key(compare))

a,b = 0,0
for i,x in enumerate(sorted_packets, 1):
    if x == [[2]]:
        a = i
    if x == [[6]]:
        b = i

print(a*b)