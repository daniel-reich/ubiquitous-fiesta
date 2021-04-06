
def climbing_leaderboard(ranked, player):
  a=set(ranked)
  ranked=list(a)
  x=[]
  for i in player:
    y=len(ranked)+1
    for j in ranked:
      if i>=j:
        y-=1
    x.append(y)
  return x

