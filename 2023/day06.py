import re
times, distances = (tuple(map(int,re.findall(r'(\d+)', line))) for line in open("input"))

ans = 1
for time, win_distance in zip(times,distances):
    a = 0
    for speed in range(time):
        distance = speed * (time-speed)
        if distance > win_distance:
            a += 1
    ans *= a
print(ans)

time, distance = map(int,(''.join(re.findall(r'(\d+)', line)) for line in open("input")))
from sympy import *

x,y,z = symbols("x y z")
a,b = solveset(Eq(time*x-x**2, distance), x)
ans = int(b) - int(a)
print(ans)