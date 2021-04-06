
def climbing_leaderboard(ranked, player):
  lst=[]
  for i in player:
    ranked.append(i)
    l=sorted(set(ranked),reverse=True)
    a=l.index(i)
    lst.append(a+1)
  return lst

