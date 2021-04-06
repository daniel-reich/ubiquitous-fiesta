
def climbing_leaderboard(ranked, player):
    ans = []
    for score in player:
        ans.append(1 + len(set([r for r in ranked if r > score])))
    return ans

