
def climbing_leaderboard(ranked, player):
  ranked  = set(ranked)
  place = lambda score: sum(1 for record in ranked if record > score) + 1
  return [place(s) for s in player]

