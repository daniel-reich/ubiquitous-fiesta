
from collections import Counter
def yahtzee_score_calc(lst):
    score = 0
    score_first_phase = 0
    score += lst[0].count(1) + lst[1].count(2) * 2 + lst[2].count(3) * 3 + lst[3].count(4) * 4 + lst[4].count(5) * 5 + lst[5].count(6) * 6
    score_first_phase = score
    if 3 in Counter(lst[6]).values() or 4 in Counter(lst[6]).values() or 5 in Counter(lst[6]).values() or 6 in Counter(lst[6]).values():
        score += sum(lst[6])
    if 4 in Counter(lst[7]).values() or 5 in Counter(lst[7]).values() or 6 in Counter(lst[7]).values():
        score += sum(lst[7])
    if len(Counter(lst[8])) == 2 and 2 in Counter(lst[8]).values() and 3 in Counter(lst[8]).values():
        score += 25
    if {1, 2, 3, 4} <= set(lst[9]) or {2, 3, 4, 5} <= set(lst[9]) or {3, 4, 5, 6} <= set(lst[9]):
        score += 30
    if {1, 2, 3, 4, 5} <= set(lst[10]) or {2, 3, 4, 5, 6} <= set(lst[10]):
        score += 40
    if len(Counter(lst[11])) == 1:
        score += 50
    score += sum(lst[12])
    if score_first_phase >= 63:
        return score + 35
    return score

