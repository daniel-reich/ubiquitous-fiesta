
from bisect import bisect
def climbing_leaderboard(ranked, player):
  ranked = sorted(set(ranked))
  return [len(ranked)+1-bisect(ranked,p) for p in player]

