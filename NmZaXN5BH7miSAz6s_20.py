
def climbing_leaderboard(ranked, player):
    ranking = [1]
    myans = []
    a = 1
    for i in range(1,len(ranked)):
        if ranked[i] == ranked[i-1]:
            ranking.append(a)
        else:
            a+=1
            ranking.append(a)
​
    for j in player:
        ranked.append(j)
        ranked = sorted(ranked,reverse=True)
​
        a = 1
        ranking = [1]
        for i in range(1,len(ranked)):
            if ranked[i] == ranked[i-1]:
                ranking.append(a)
            else:
                a+=1
                ranking.append(a)
        b = ranked.index(j)
        myans.append(ranking[b])
​
    return myans

