
def climbing_leaderboard(ranked, player):
  lb = []
  for score in ranked:
    if not score in lb: lb.append(score)
  ranks = []
  for round in player:
    added = False
    for score in lb:
      if round >= score:
        ranks.append(lb.index(score) + 1)
        added = True
        break
    if not added: ranks.append(len(lb) + 1)
  return ranks

