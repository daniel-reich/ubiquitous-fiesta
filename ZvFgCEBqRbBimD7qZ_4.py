
def bowling(pins):
    score = [0,0,0,0,0,0,0,0,0,0]
    f = 0
    i = 0
    while f < 10:
        if pins[i] == 10:
            score[f] = pins[i]+pins[i+1]+pins[i+2]
            i += 1
        elif pins[i] + pins[i+1] == 10:
            score[f] = pins[i]+pins[i+1]+pins[i+2]
            i += 2
        else:
            score[f] = pins[i] + pins[i+1]
            i += 2
        f += 1
        
    return sum(score)

