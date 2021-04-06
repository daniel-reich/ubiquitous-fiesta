
def yahtzee_score_calc(lst):
​
    myscoreA = 0
    myscoreB = 0
    for i in range(1,7):
        myscoreA += lst[i-1].count(i)*i
​
    if myscoreA >= 63:
        myscoreA += 35
​
    for i in range(6,13):
        if i == 6:
            for j in range(3):
                if lst[i].count(lst[i][j]) >= 3:
                    myscoreB += sum(lst[i])
                    break
        if i == 7:
            for j in range(2):
                if lst[i].count(lst[i][j]) >= 4:
                    myscoreB += sum(lst[i])
                    break
        if i == 8:
            if len(set(lst[i])) == 2:
                myscoreB += 25
​
        if i == 9:
            lst[i] = sorted(lst[i])
            if (lst[i][4] - lst[i][1] == 3 and len(set(lst[i][1:])) == 4 ) or (lst[i][3] - lst[i][0] == 3 and len(set(lst[i][:4])) == 4 ):
                myscoreB += 30
​
        if i == 10:
            lst[i] = sorted(lst[i])
            if lst[i][4] - lst[i][0] == 4 and len(set(lst[i])) == 5:
                myscoreB += 40
​
        if i == 11:
            if len(set(lst[i])) == 1:
                myscoreB += 50
​
        if i == 12:
            myscoreB += sum(lst[i])
​
    return myscoreA + myscoreB

