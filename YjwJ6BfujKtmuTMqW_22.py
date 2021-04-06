
def dice_game(scores):
  players='1234'
  while len(players)>1:
    p=[scores[i] for i in range(len(players))]
    sc=[i[0]+i[1] for i in p]
    scores=scores[len(players):]
    if sc.count(min(sc))==1:
      ind=sc.index(min(sc))
      players = players[:ind]+players[ind+1:]
    else:
      lowplayers = ''.join([str(i) for i in range(len(sc)) if sc[i]==min(sc)])
      lowdie = [p[int(i)][0] for i in lowplayers]
      if lowdie.count(min(lowdie))==1:
        ind=int(lowplayers[lowdie.index(min(lowdie))])
        players = players[:ind]+players[ind+1:]
  return 'p'+players

