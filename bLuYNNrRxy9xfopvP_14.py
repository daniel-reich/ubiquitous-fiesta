
from collections import Counter
​
def yahtzee_score_calc(lst):
    points = 0
    for k in range(1, 7):
        points += k * lst[k -1].count(k)
    if points >= 63:
        points += 35
    C = Counter(lst[6])
    if max(list(C.values())) >= 3:
        points += sum(lst[6])
    C = Counter(lst[7])
    if max(list(C.values())) >= 4:
        points += sum(lst[7])
    C = Counter(lst[8])
    if 2 in C.values() and 3 in C.values():
        points += 25
    row = sorted(lst[9])
    if row[:4] in [[1,2,3,4], [2,3,4,5], [3,4,5,6]] or \
       row[1:] in [[1,2,3,4], [2,3,4,5], [3,4,5,6]]:
        points += 30
    row = sorted(lst[10])
    if row == [1,2,3,4,5] or row == [2,3,4,5,6]:
        points += 40
    if len(set(lst[11])) == 1:
        points += 50
    points += sum(lst[12])
    return points

