import re

ans = 0
for line in open("input"):
    a,b = line.split(':')[1].split('|')
    win,you = map(set, (re.findall("\d+", a), re.findall("\d+", b)))
    nr = len(win & you)
    if nr > 0:
        ans += 2**(nr-1)
print(ans)

card_map = {}
for i,line in enumerate(open("input"),1):
    a,b = line.split(':')[1].split('|')
    win,you = map(set, (re.findall("\d+", a), re.findall("\d+", b)))
    n = len(win & you)
    card_map[i] = tuple(range(i+1,i+1+n))

def fun(cards):
    c = len(cards)
    for card in cards:
        c += fun(card_map[card])
    return c

ans = 0
for cards in card_map.values():
    ans += fun(cards) + 1
print(ans)