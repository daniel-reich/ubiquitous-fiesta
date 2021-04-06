
def dice_score(throw):
    score = 0
    ones, twos, threes, fours, fives, sixes = 0, 0, 0, 0, 0, 0
    for i in throw:
        if i == 1:
            ones += 1
        elif i == 2:
            twos += 1
        elif i == 3:
            threes += 1
        elif i == 4:
            fours += 1
        elif i == 5:
            fives += 1
        elif i == 6:
            sixes += 1
​
    if ones >= 3:
        score += 1000
        ones - 3
    elif twos >= 3:
        score += 200
        twos - 3
    elif threes >= 3:
        score += 300
        threes - 3
    elif fours >= 3:
        score += 400
        fours - 3
    elif fives >= 3:
        score += 500
        fives - 3
    elif sixes >= 3:
        score += 600
        sixes - 3
​
    score += 50 * fives
    score += 100 * ones
​
    return score

