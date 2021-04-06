
def climbing_leaderboard(ranked, player):
  result = []
  for score in player:
    leaderboards = ranked
    leaderboards.append(score)
    leaderboards = list(dict.fromkeys(leaderboards))
    leaderboards = sorted(leaderboards)
    leaderboards.reverse()
    for gliga in leaderboards:
      if gliga == score:
        result.append(leaderboards.index(gliga)+1)
  return result

