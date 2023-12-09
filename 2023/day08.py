import re, math

directions, elements = open("input").read().split('\n\n')
directions = directions.translate(str.maketrans({'L':'0', 'R': '1'}))
network = {k:(l,r) for (k,l,r) in re.findall(r'(.+) = \((.+), (.+)\)', elements)}

start = [x for x in network.keys() if x.endswith('A')]
goal = set(x for x in network.keys() if x.endswith('Z'))

ans = []
for cur in start:
    steps = 0
    while cur not in goal:
        for direction in map(int,directions):
            cur = network[cur][direction]
            steps += 1
    ans += [steps]

print(ans[start.index('AAA')])
print(math.lcm(*ans))