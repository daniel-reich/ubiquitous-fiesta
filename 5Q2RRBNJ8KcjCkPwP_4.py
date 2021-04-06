
def tic_tac_toe(inputs):
  A=[list(x) for x in zip(*inputs)]
  B=[[inputs[i][i] for i in range(3)]]
  C=[[inputs[i][2-i] for i in range(3)]]
  S=inputs+A+B+C
  if ['X']*3 in S:
    return "Player 1 wins"
  elif ['O']*3 in S:
    return "Player 2 wins"
  else:
    return "It's a Tie"

