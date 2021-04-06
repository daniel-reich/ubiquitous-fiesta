
def check_score(s):
    score = 0
    for i in s:
        for j in i:
            if j == '#':
                score += 5
            elif j == 'O':
                score += 3
            elif j == 'X':
                score += 1
            elif j == '!':
                score -= 1
            elif j == '!!':
                score -= 3
            elif j == '!!!':
                score -= 5
    if str(score).count('-') != 0:
        return 0
    else:
        return score

