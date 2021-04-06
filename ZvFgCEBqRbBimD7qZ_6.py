
def bowling(pins):
    score = 0
    bowl = 0
    for frame in range(1, 11):
        if pins[bowl] == 10:
            score += (pins[bowl] + pins[bowl+1] + pins[bowl+2])
            bowl += 1
        else:
            if pins[bowl] + pins[bowl+1] == 10:
                score += (pins[bowl] + pins[bowl+1] + pins[bowl+2])
                bowl += 2
            else:
                score += (pins[bowl] + pins[bowl+1])
                bowl += 2
    return score

