
def climbing_leaderboard(ranked, player):
  return [ranking(ranked, play) for play in player]
def ranking(ranked, score):
  ranked.append(score)
  lst = sorted(list(set(ranked)), reverse = True)
  return lst.index(score) +1

