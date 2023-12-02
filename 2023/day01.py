import re

p1 = sum(int(ds[0] + ds[-1]) for ds in (re.findall(r'\d', line) for line in open("input")))
print(p1)

digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
capture = '|'.join(list(digits.keys()) + ['\d'])
rgx = rf'(?=({capture}))'
c = lambda x: digits[x] if x in digits else int(x)
p2 = sum((int(str(c(a)) + str(c(b))) for (a,b) in ((ds[0], ds[-1]) for ds in (re.findall(rgx, line) for line in open("input")))))
print(p2)