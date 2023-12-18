import re
from collections import defaultdict

boxes = defaultdict(lambda: [])
p1 = 0
p2 = 0

def hhash(label):
    res = 0
    for char in label:
        n = ord(char)
        res += n
        res *= 17
        res %= 256
    return res

for step in open("input").read().rstrip().split(','):
    p1 += hhash(step)
    label,op = re.split(r"=|-",step)
    hs = hhash(label)
    idx = next((i for i,(a,b) in enumerate(boxes[hs]) if a == label), None)
    if "=" in step:
        if idx is not None:
            boxes[hs][idx] = label,int(op)
        else:
            boxes[hs].append((label,int(op)))
    elif idx is not None:
        boxes[hs].pop(idx)

for box,val in boxes.items():
    for i,(_,focus) in enumerate(val,1):
        p2 += (box+1) * i * focus

print(p1)
print(p2)