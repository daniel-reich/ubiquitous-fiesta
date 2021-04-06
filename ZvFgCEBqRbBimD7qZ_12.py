
def bowling(pins):
    i,score=0,[]
    while len(score)<10:
        if pins[i] == 10:
            score+=[sum(pins[i:i+3])]
            i+=1
        elif pins[i]+pins[i+1]==10:
            score+=[sum(pins[i:i+3])]
            i+=2
        else:
            score+=[pins[i]+pins[i+1]]
            i+=2
    return sum(score)

