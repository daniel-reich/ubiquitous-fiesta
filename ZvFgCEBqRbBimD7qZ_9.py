
def bowling(pins):
    score=0; i=0
    try:
        for item in pins[:-2]:
            if pins[i]==10:
                score+=10+pins[i+1]+pins[i+2]
                i+=1
            elif pins[i]+pins[i+1] ==10:
                score+=10+pins[i+2]
                i+=2
            else:
                score+=pins[i]+pins[i+1]
                i+=2
        return score
    except IndexError:
        return score

