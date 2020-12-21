#!/usr/bin/env python
import itertools as it
import re
from collections import defaultdict

lines = [line.rstrip() for line in open('input')]

allergens = {}
all_ingredients = []

for line in lines:
    words = re.findall(r'(\w+)', line)
    delimiter = words.index('contains')

    ingredients = words[:delimiter]
    all_ingredients += ingredients
    for allergen in words[delimiter+1:]:
        if allergen in allergens:
            allergens[allergen] &= set(ingredients)
        else:
            allergens[allergen] = set(ingredients)


bad = set().union(*allergens.values())

ans = sum(1 for ingredient in all_ingredients if ingredient not in bad)

print(ans)

exclude = set()
ans = []
while len(allergens) != len(exclude):
    for allergen, ingredients in allergens.items():
        if len(a := (ingredients - exclude)) == 1:
            a = a.pop()
            ans += [(a, allergen)]
            exclude.add(a)

print(",".join(a[0] for a in sorted(ans, key=lambda x: x[1])))