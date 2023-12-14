from functools import cache

def join(parts):
    if not parts[1:]:
        return parts[0]
    return (*parts[0],2,*join(parts[1:]))

@cache
def f(springs, sizes):
    result = 0
    cur,sizes = sizes[0],sizes[1:]

    for i in range(100):
        nxt = cur + i
        if 1 in springs[:i] or nxt > len(springs):
            break

        if 0 in springs[i:nxt] or (nxt in range(len(springs)) and springs[nxt] == 1):
            continue

        if not sizes:
            result += 1 not in springs[nxt+1:]

        result += len(sizes) and f(springs[nxt+1:], sizes)
    return result

p1 = 0
p2 = 0
for line in map(str.rstrip, open("input")):
    springs, sizes = line.split()
    sizes = tuple(int(s) for s in sizes.split(','))
    springs = tuple(int(s) for s in springs.translate(str.maketrans({'?':'2','.':'0','#':'1'})))

    p1 += f(springs, sizes)
    p2 += f(join([springs]*5), sizes*5)

print(p1)
print(p2)