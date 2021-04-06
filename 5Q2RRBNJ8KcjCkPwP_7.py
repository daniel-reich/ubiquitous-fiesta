
import numpy as np
​
def tic_tac_toe(inputs):
  i = np.array(inputs)
  lines = np.r_[i, i.T, [np.diag(i)], [np.diag(np.rot90(i))]]
  return {"X": "Player 1 wins", "O": "Player 2 wins"}.get(([l[0] for l in lines if len(set(l)) == 1] or ["_"])[0], "It's a Tie")

