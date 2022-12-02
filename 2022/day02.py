#!/usr/bin/env python3.10

rounds = [line.split() for line in open("input")]

counter_move = [2, 0, 1]
opp_moves = ['A', 'B', 'C']
your_moves = ['X', 'Y', 'Z']

p1, p2 = (0,0)
for (opp, you) in rounds:
    opp = opp_moves.index(opp)
    you = your_moves.index(you)

    # part 1
    p1 += you+1
    if you == opp:
        # draw
        p1 += 3
    elif opp == counter_move[you]:
        # win
        p1 += 6

    # part 2
    if you == 0:
        # loose
        p2 += counter_move[opp]+1
    elif you == 1:
        # draw
        p2 += opp + 1 + 3
    elif you == 2:
        # win
        p2 += counter_move.index(opp) + 1 + 6

print(p1)
print(p2)