#!/usr/bin/env python
import itertools as it5
import re

player1, player2 = [list(map(int,e.rstrip().split('\n')[1:])) for e in open('input').read().split('\n\n')]

def combat(player1, player2):
    configurations = set()
    while len(player1) and len(player2):
        if (tuple(player1), tuple(player2)) in configurations:
            return True

        configurations.add((tuple(player1), tuple(player2)))
        a,b = player1.pop(0), player2.pop(0)

        if a <= len(player1) and b <= len(player2):
            if combat(player1[:a], player2[:b]):
                player1.extend([a,b])
            else:
                player2.extend([b,a])
            continue

        if a > b:
            player1.extend([a,b])
        else:
            player2.extend([b,a])

    return len(player1) > len(player2)

combat(player1, player2)

winner = max(player1,player2)
ans = sum(card * val for card,val in zip(winner,range(len(winner),0,-1)))

print(ans)