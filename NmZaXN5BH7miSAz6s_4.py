
def rank(r, p):
    r.append(p)
    return sorted(r)[::-1].index(p)+1
def climbing_leaderboard(ranked, player):
    ranked = list(set(ranked))
    return [rank(ranked, i) for i in player]

