
def climbing_leaderboard(ranked, player):
    r = []
    for i in player:
        s = ranked.copy()
        s.append(i)
        rank = sorted(list(set(s)), reverse=True).index(i)
        r.append(rank + 1)
    return r

