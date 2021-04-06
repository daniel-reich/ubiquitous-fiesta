
def play_round (P1, P2, P3, P4):
  ptotals = [P1[0]+P1[1],P2[0]+P2[1],P3[0]+P3[1],P4[0]+P4[1]]
  pfirsts = [P1[0],P2[0],P3[0],P4[0]]
  m = min(ptotals)
  if (ptotals.count(m)==1):
    return(('p1' if ptotals[0]==m else 'p2' if ptotals[1]==m 
    else 'p3' if ptotals[2]==m else 'p4'))
  else:
    pfirsts[0] = (7 if ptotals[0] != m else P1[0])
    pfirsts[1] = (7 if ptotals[1] != m else P2[0])
    pfirsts[2] = (7 if ptotals[2] != m else P3[0])
    pfirsts[3] = (7 if ptotals[3] != m else P4[0])
    n = min(pfirsts)
    if (pfirsts.count(n) > 1):
      return ('')
    else:
      return(('p1' if pfirsts[0]==n else 'p2' if pfirsts[1]==n 
      else 'p3' if pfirsts[2]==n else 'p4'))
​
def dice_game(scores):
  players_in = 4
  play_rolls = {'p1':(0,0) ,'p2': (0,0),'p3':(0,0) ,'p4':(0,0)}
  play_in = {'p1': True, 'p2': True, 'p3': True, 'p4': True}
  while players_in > 1:
    play_rolls['p1'] = (scores[0] if play_in['p1']==True else (7,7))
    if play_in['p1']==True : scores.pop(0) 
    play_rolls['p2'] = (scores[0] if play_in['p2']==True else (7,7))
    if play_in['p2']==True : scores.pop(0) 
    play_rolls['p3'] = (scores[0] if play_in['p3']==True else (7,7))
    if play_in['p3']==True : scores.pop(0) 
    play_rolls['p4'] = (scores[0] if play_in['p4']==True else (7,7))
    if play_in['p4']==True : scores.pop(0) 
    loser = play_round(play_rolls['p1'],play_rolls['p2'],play_rolls['p3'],play_rolls['p4'])
    if (loser != ''):
      play_in[loser] = False
      players_in -= 1
  return ('p1' if play_in['p1']==True else 'p2' if play_in['p2']==True 
  else 'p3' if play_in['p3']==True else 'p4' )

