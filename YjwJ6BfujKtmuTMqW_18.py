
def dice_game(scores,player=["p1","p2","p3","p4"]):
  dice = [scores[i] for i in range(len(player))]
  ref1 = [sum(scores[i]) for i in range(len(player))]
  ref2 = [sum(scores[i]) + scores[i][0] for i in range(len(player))] 
  
  g_player  = []
  for i in range(len(player)):
    if ref1[i] == min(ref1) and dice.count(dice[i])>1:
      g_player = player
      break
    elif ref1[i] > min(ref1):
      g_player.append(player[i])
    elif ref1[i] == min(ref1) and ref1.count(min(ref1)) > 1:
      if ref2[i] > min(ref2):
        g_player.append(player[i])
  if len(g_player)==1:
    res = "".join(g_player)
    return res
  else:
    return dice_game(scores[len(player):],g_player)

