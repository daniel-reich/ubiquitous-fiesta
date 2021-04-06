
def currently_winning(scores):
  currently_winner= []
  myscore, opponentscore= 0,0
  for i in range(0, len(scores), 2):
    myscore+= scores[i]
    opponentscore += scores[i+1]
    
    if myscore > opponentscore:
      winner = 'Y'
    elif myscore < opponentscore:
      winner = 'O'
    else:
      winner = 'T'
    
    currently_winner.append(winner)
    
  return currently_winner

