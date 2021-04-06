
def champions(team):
    topscore = 0
    winner = {}
    for i in range(len(team)):
        a = 3 * team[i]['wins'] + 0 * team[i]['loss'] + 1 * team[i]['draws']
        if a>topscore:
            topscore = a
            winner[team[i]['name']] = a
        elif a == topscore:
            winner[team[i]['name']] = a
            winner = {team[j]['name']:team[j]['scored'] - team[j]['conceded'] for j in range(len(team)) if team[j]['name'] in winner}
            
    return max(winner,key=winner.get)

