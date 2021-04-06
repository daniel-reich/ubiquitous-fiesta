
import numpy as np
winner = {'X':"1",'O':"2"}
​
def tic_tac_toe(inputs):
  inputs_np = np.array(inputs)
  inputs_diag = np.diag(inputs_np).tolist()
  inputs_col = np.rot90(inputs_np)
  inputs_col_lst = inputs_col.tolist()
  inputs_diag2 = np.diag(inputs_col).tolist()
  if len(set(inputs_diag)) == 1:
    return "Player {} wins".format(winner[inputs[0][0]])
  elif len(set(inputs_diag2)) == 1:
    return "Player {} wins".format(winner[inputs[0][2]])
  else:
    for i in range(0,3):
      if len(set(inputs[i])) == 1:
        return "Player {} wins".format(winner[inputs[i][0]])
      elif len(set(inputs_col_lst[i])) == 1:
        return "Player {} wins".format(winner[inputs_col_lst[i][0]])
    return "It's a Tie"

