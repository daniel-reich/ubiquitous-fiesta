
def tic_tac_toe(inputs):
  lines = inputs + list(map(list, zip(*inputs))) \
    + [[inputs[i][i] for i in range(3)], [inputs[2-i][i] for i in range(3)]]
  if ['X', 'X', 'X'] in lines: return "Player 1 wins"
  if ['O', 'O', 'O'] in lines: return "Player 2 wins"
  return "It's a Tie"

