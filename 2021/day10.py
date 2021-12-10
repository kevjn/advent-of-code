#!/usr/bin/env python3.9

lines = [line.rstrip() for line in open('input')]

p1 = 0
scores = []
for line in lines:
    s = []
    for ch in line:
        if ch in '([{<':
            s.append(ch)
        else:
            if ch != ')]}>'['([{<'.index(s.pop())]:
                p1 += [3, 57, 1197, 25137][')]}>'.index(ch)]
                break
    else:
        score = 0
        for p in [[1,2,3,4]['([{<'.index(x)] for x in s[::-1]]:
            score *= 5
            score += p

        scores.append(score)

p2 = sorted(scores)[len(scores)//2]

print(p1)
print(p2)