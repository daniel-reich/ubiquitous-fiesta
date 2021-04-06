
def isWinner(inputs):
  for l in inputs + list(zip(*inputs)):
    if len(set(l)) == 1: return l[0]
  if inputs[0][0] == inputs[1][1] == inputs[2][2]: return inputs[1][1]
  if inputs[2][0] == inputs[1][1] == inputs[0][2]: return inputs[1][1]
  return ""
  
def tic_tac_toe(inputs):
  res = isWinner(inputs);
  return ("Player " + str(1 + int(res == 'O')) + " wins") if res else "It's a Tie"

