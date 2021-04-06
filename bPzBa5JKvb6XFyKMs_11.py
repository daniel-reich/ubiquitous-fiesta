
def calcScore(v):
    if v == 'A':
        return 16
    if v == 'K' or v == 'Q' or v == 'J':
        return 10
    if 2 <= int(v) <= 5:
        return 10+int(v)
    if v == '6':
        return 18    
    if v == '7':
        return 21
    
def get_primiera_score(deck):
    #[Hearts,Diamonds,Spades,Clubs]
    myScore = [-1,-1,-1,-1]
    
    for item in deck:
        if item[1] == 'h':
            s = calcScore(item[0])
            if s > myScore[0]:
                myScore[0] = s   
        elif item[1] == 'd':
            s = calcScore(item[0])
            if s > myScore[1]:
                myScore[1] = s
        elif item[1] == 's':
            s = calcScore(item[0])
            if s > myScore[2]:
                myScore[2] = s
        else:
            s = calcScore(item[0])
            if s > myScore[3]:
                myScore[3] = s            
    if -1 in myScore:
        return 0
    else:
        return sum(myScore)

