
def tournament_scores(scores):
    '''
    Returns the result of the tournament games in scores as per instructions
    '''
    table = {}
​
    for score in scores:
        us, ours, theirs, them = score.replace('-','').split()
        ours = int(ours)
        theirs = int(theirs)
        home = table.get(us, [0,0,0])
        away = table.get(them, [0,0,0])
        our_points = 3 if ours > theirs else 1 if ours == theirs else 0
        their_points = 3 if theirs > ours else 1 if theirs == ours else 0
        table[us] = [home[0]+our_points, home[1]+ours, home[2]+ours-theirs]
        table[them] = [away[0]+their_points, away[1]+theirs, away[2]+theirs-ours]
​
    return sorted([[team,v[0],v[1],v[2]] for team,v in table.items()],
                  key=lambda x: (x[1],x[2],x[3]), reverse=True)

