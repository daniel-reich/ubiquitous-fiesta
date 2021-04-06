
def climbing_leaderboard(ranked, player):
  get_rank = lambda pts: len([r for r in set(ranked) if pts<r]) + 1
  return [get_rank(pts) for pts in player]

