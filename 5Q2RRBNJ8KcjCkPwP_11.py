
def tic_tac_toe(inputs):
  player = 0
  if inputs[0][0]== inputs[1][1] and inputs[2][2]==inputs[0][0]:
    if inputs[0][0]=="X":
      player=1
    else:
      player=2
  elif inputs[0][2]==inputs[1][1] and inputs[2][0]==inputs[0][2]:
    if inputs[1][1]=="X":
      player=1
    else:
      player=2
  elif inputs[0][0]==inputs[0][1] and inputs[0][2]==inputs[0][0]:
    if inputs[0][0]=="X":
      player=1
    else:
      player=2
  elif inputs[1][0]==inputs[1][1] and inputs[1][2]==inputs[1][0]:
    if inputs[1][1]=="X":
      player=1
    else:
      player=2
  elif inputs[2][0]==inputs[2][1] and inputs[2][2]==inputs[2][0]:
    if inputs[2][2]=="X":
      player=1
    else:
      player=2
  elif inputs[0][0]==inputs[1][0] and inputs[2][0]==inputs[0][0]:
    if inputs[0][0]=="X":
      player=1
    else:
      player=2
  elif inputs[0][1]==inputs[1][1] and inputs[2][1]==inputs[0][1]:
    if inputs[1][1]=="X":
      player=1
    else:
      player=2
  elif inputs[0][2]==inputs[1][2] and inputs[2][2]==inputs[0][2]:
    if inputs[2][2]=="X":
      player=1
    else:
      player=2
  else:
    player=0
  
  if player==1:
    return "Player 1 wins"
  elif player==2:
    return "Player 2 wins"
  else:
    return "It's a Tie"

