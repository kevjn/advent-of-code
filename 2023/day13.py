import numpy as np
import itertools as it

def divide_arr(arr):
    right = arr[:,i:]
    left = arr[:,:i][:,::-1]
    size = min(right.shape[1],left.shape[1])
    return left[:,:size] ,right[:,:size]

p1,p2 = 0,0
for block in open("input").read().split('\n\n'):
    arr  = np.array([[True if c == '#' else False for c in line] for line in block.split()])

    seen = set()
    for m in (1,100):
        for i in reversed(range(1,arr.shape[1])):
            left,right = divide_arr(arr)
            if (left == right).all():
                p1 += i * m
                seen.add(i*m)
                break
        arr = np.rot90(arr)
    arr = np.rot90(arr,2)

    for smudge in it.product(range(arr.shape[0]), range(arr.shape[1])):
        smudged_arr = arr.copy()
        smudged_arr[smudge] = ~smudged_arr[smudge]
        for m in (1,100):
            for i in reversed(range(1,smudged_arr.shape[1])):
                smudged_left,smudged_right = divide_arr(smudged_arr)
                if (smudged_left == smudged_right).all():
                    if i*m in seen:
                        continue
                    p2 += i * m
                    seen.add(i*m)
                    break
            smudged_arr = np.rot90(smudged_arr)

print(p1,p2)