
def climbing_leaderboard(ranked, player):
    a1 = []
    ranked = list(set(ranked))
    for i in range(len(player)):
        ranked.append(player[i])
​
        ranked.sort(reverse = True)
        b1 = ranked.index(player[i])
        a1.append( b1 + 1 )
        ranked.remove(player[i])
​
    return a1

