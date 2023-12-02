import re
import math

games = [line.split(':')[1].split(";") for line in open("input")]

fun = lambda x: x.group(1) if x else '0'

ans = 0
for i,game in enumerate(games,1):
    for cubes in game:
        r,g,b = (int(fun(re.search(rf'(\d+) {color}', cubes))) for color in ('red','green','blue'))
        if (r > 12 or g > 13 or b > 14):
            ans -= i
            break

    ans += i
print(ans)

ans = 0
for i,game in enumerate(games,1):
    mincolors = 0,0,0
    for cubes in game:
        colors = [int(fun(re.search(rf'(\d+) {color}', cubes))) for color in ('red','green','blue')]
        mincolors = [max(c,mc) for (c,mc) in zip(colors, mincolors)]
    
    ans += math.prod(mincolors)
print(ans)