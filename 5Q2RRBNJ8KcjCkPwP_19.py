
def tic_tac_toe(g):
  winner = ""
  boolean = True
  
  h0 = g[0][0] == g[0][1] and g[0][0] == g[0][2]
  h1 = g[1][0] == g[1][1] and g[1][0] == g[1][2] 
  h2 = g[2][0] == g[2][1] and g[2][0] == g[2][2]
  
  v0 = g[0][0] == g[1][0] and g[0][0] == g[2][0]
  v1 = g[0][1] == g[1][1] and g[0][1] == g[2][1] 
  v2 = g[0][2] == g[1][2] and g[0][2] == g[2][2]
  
  d0 = g[0][0] == g[1][1] and g[0][0] == g[2][2]
  d1 = g[0][2] == g[1][1] and g[0][2] == g[2][0]
  
  if boolean in [h1, v1, d0, d1]:
    winner = g[1][1]
  elif boolean in [v0, h0]:
    winner = g[0][0]
  elif boolean in [h2, v2]:
    winner = g[2][2]
  else:
    winner = "#"
  
  if winner == "X":
    return "Player 1 wins"
  elif winner == "O":
    return "Player 2 wins"
  else:
    return "It's a Tie"

