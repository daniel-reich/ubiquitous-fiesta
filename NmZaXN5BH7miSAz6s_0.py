
def climbing_leaderboard(ranked, player):
    return [sorted(set(ranked + [i]), reverse=True).index(i) + 1 for i in player]

