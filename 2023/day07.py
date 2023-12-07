hand_fxs = [
    lambda x: len(x) == 1,
    lambda x: any(v == 4 for v in x),
    lambda x: any(v == 3 for v in x) and any(v == 2 for v in x),
    lambda x: any(v == 3 for v in x),
    lambda x: sum(v == 2 for v in x) == 2,
    lambda x: any(v == 2 for v in x),
    lambda x: len(x) == 5,
]

hands = [line.strip().split() for line in open("input")]

CARD_TYPES = 'AKQJT98765432'[::-1]

def rank_fxn(game):
    hand,bid = game
    counts = [hand.count(c) for c in set(hand)]
    for i,f in enumerate(hand_fxs):
        if f(counts):
            return 7-i, [CARD_TYPES.index(c) for c in hand]
    else:
        raise Exception()

sorted_hands = sorted(hands, key=rank_fxn)

ans = 0
for rank, (hand, bid) in enumerate(sorted_hands,1):
    ans += rank * int(bid)
print(ans)

CARD_TYPES = 'AKQT98765432J'[::-1]

def rank_fxn(game):
    hand,bid = game
    counts = {c: hand.count(c) for c in set(hand)}
    if 'J' in counts.keys():
        maxk = max(counts, key=lambda k: counts.get(k) if k != 'J' else 0)
        counts[maxk] += counts['J']
        del counts['J']
        if not counts:
            counts = {'J': 5}

    for i,f in enumerate(hand_fxs):
        if f(counts.values()):
            return 7-i, [CARD_TYPES.index(c) for c in hand]
    else:
        raise Exception()

sorted_hands = sorted(hands, key=rank_fxn)

ans = sum(rank*int(bid) for (rank, (hand, bid)) in enumerate(sorted_hands,1))
print(ans)