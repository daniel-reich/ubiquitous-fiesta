
def climbing_leaderboard(ranked, player):
  ret=[]
  for i in player:
    ranked.append(i)
    ranked = sorted(list(set(ranked)))[::-1]
    ret.append(ranked.index(i)+1)
  return ret

