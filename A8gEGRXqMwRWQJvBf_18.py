
def tic_tac_toe(b):
  for l in b + list(zip(*b)):
    if len(set(l))==1:
      return l[0]
  x1 = set(b[0][0] + b[1][1] + b[2][2])
  x2 = set(b[0][2] + b[1][1] + b[2][0])
  if 1 in [len(x1),len(x2)]:
    return b[1][1]
  return "Draw"

