
def champions(teams):
    lst=[]
    c=0
    while c < len(teams):
        points=0
        score=0
        points+=teams[c]["wins"]*3
        points+=teams[c]["draws"]*1
        score+=teams[c]["scored"]-teams[c]["conceded"]
        lst.append([teams[c]["name"],points,score])
        c+=1
    points=0
    score=0
    winner=""
    wc=0
    res=[]
    for i in range(0, len(lst)):
        if lst[i][1] > points:
            points=lst[i][1]
            res=[lst[i]]
            wc+=1
        elif lst[i][1] == points:
            res.append(lst[i])
    if wc==1:
        return res[0][0]
    else:
        for i in range(0,len(res)):
            if res[i][2] > score:
                score=res[i][2]
                winner=res[i][0]
            else:
                pass
        return winner

