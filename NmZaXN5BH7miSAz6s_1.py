
from bisect import bisect_right
def climbing_leaderboard(ranked, player):
  ranked = sorted(set(ranked))
  return [len(ranked)+1-bisect_right(ranked, play) for play in player]

