
def climbing_leaderboard(ranked, player):
  A=[]
  for x in player:
    ranked=sorted(set(ranked+[x]), reverse=True)
    A.append(ranked.index(x)+1)
  return A

