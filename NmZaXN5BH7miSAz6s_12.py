
def climbing_leaderboard(ranked, player):
    res = []
    for p_score in player:
        scores = sorted(ranked + [p_score], reverse=True)
        rank = 1
        for i, s in enumerate(scores):
            if i > 0 and s < scores[i - 1]:
                rank += 1
            if s == p_score:
                res.append(rank)
                break
    return res

