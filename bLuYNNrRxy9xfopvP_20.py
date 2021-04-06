
def yahtzee_score_calc(lst):
    score = sum(lst[i].count(i+1)*(i+1) for i in range(6))
    score += 35 if score >= 63 else 0
    score += sum(lst[6]) if 3 in [lst[6].count(i) for i in set(lst[6])] else 0
    score += sum(lst[7]) if 4 in [lst[7].count(i) for i in set(lst[7])] or 5 in [lst[7].count(i) for i in set(lst[7])] else 0
    score += 25 if len(set(lst[8])) == 2 else 0
    lst[9].sort()
    score += 30 if (lst[9][0]==lst[9][1]-1==lst[9][2]-2==lst[9][3]-3 or lst[9][1]==lst[9][2]-1==lst[9][3]-2==lst[9][4]-3) else 0
    score += 40 if sorted(lst[10]) == [1,2,3,4,5] or sorted(lst[10]) == [2,3,4,5,6] else 0
    score += 50 if lst[11].count(lst[11][0]) == 5 else 0
    return score + sum(lst[12])

