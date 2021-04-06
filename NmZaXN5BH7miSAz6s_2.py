
def climbing_leaderboard(ranked,player):
    x=[]
    currentrank = len(set(ranked))
    score_index = 0
    highscore_index = len(ranked)-1
    while score_index!=len(player):
        while player[score_index] > ranked[highscore_index] and highscore_index>-1:
            highscore_index-=1
            if ranked[highscore_index]!=ranked[highscore_index+1]:
                currentrank-=1
        if player[score_index] == ranked[highscore_index]:
            x.append(currentrank) 
        else:
            x.append(currentrank+1)
        score_index+=1
    return x

