
values = {'A': 11, 'J': 10, 'Q': 10, 'K': 10, '7': 7, '8': 8, '9': 9, '10': 10}
​
def score31(c1, c2, c3):
    ranks = [c[1:] for c in [c1, c2, c3]]
    score3 = 0
    if len(set(ranks)) == 1:
        score3 = 32 if ranks[0] == 'A' else 30.5
    score_suit = 0
    for suit in "CDHS":
        score = 0
        for c in [c1, c2, c3]:
            if c[0] == suit:
                score += values[c[1:]]
        score_suit = max(score_suit, score)
    return max(score_suit, score3)

