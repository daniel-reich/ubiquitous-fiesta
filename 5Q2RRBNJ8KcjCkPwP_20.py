
def tic_tac_toe(inputs):
  pl = {"X": "1","O": "2" }
  for i in range(3):
    if inputs[i][0] == inputs[i][1] and inputs[i][1] == inputs[i][2]:
      return "Player " + pl[inputs[i][0]] + " wins"
    elif inputs[0][i] == inputs[1][i] and inputs[1][i] == inputs[2][i]:
      return "Player " + pl[inputs[0][i]] + " wins"
  if inputs[0][0] == inputs[1][1] and inputs[1][1] == inputs[2][2]:
    return "Player " + pl[inputs[1][1]] + " wins"
  elif inputs[0][2] == inputs[1][1] and inputs[1][1] == inputs[2][0]:
    return "Player " + pl[inputs[1][1]] + " wins"
  else:
    return "It's a Tie"

