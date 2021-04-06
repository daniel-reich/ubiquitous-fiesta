
def dice_game(scores):
  players = ["p1", "p2", "p3", "p4"]
  player = 0 # player in play
  lplayer = 0 # lowest scoring player for that round
  lscore = 0 # lowest round score
  die = 0 # lowest score first die
  draw = False
​
  for i in scores:
    if player == 0: # sets the new round with first players score
      draw = False
      lscore = sum(i)
      die = i[0]
      lplayer = 0     
    elif sum(i) == lscore: # checks for draws
      if i[0] == die:
        draw = True
      if i[0] < die:
        die = i[0]
        lplayer = player
​
    if sum(i) < lscore: # checks for a lower score
      lscore = sum(i)
      die = i[0]
      lplayer = player
​
    if player == len(players)-1: # ends the reound eliminating player if not lowest draw
      if draw == False or lplayer == len(players)-1:
        del players[lplayer]
      player = 0
    else:
      player += 1
​
  return players[0]

