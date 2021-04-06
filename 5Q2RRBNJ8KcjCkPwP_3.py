
import numpy as np
​
def tic_tac_toe(inputs):
  rows = np.array(inputs)
  diagonals = [[inputs[0][0], inputs[1][1], inputs[2][2]],
               [inputs[0][2], inputs[1][1], inputs[2][0]]]
  
  for row in diagonals:
    if row.count('X') == 3:
      return 'Player 1 wins'
    elif row.count('O') == 3:
      return 'Player 2 wins'
    
  if  (max(np.count_nonzero(rows == 'X', axis = 0)) == 3 or 
      max(np.count_nonzero(rows == 'X', axis = 1)) == 3):
      return 'Player 1 wins'
  elif  (max(np.count_nonzero(rows == 'O', axis = 0)) == 3 or 
      max(np.count_nonzero(rows == 'O', axis = 1)) == 3):
      return 'Player 2 wins'  
  return "It's a Tie"

