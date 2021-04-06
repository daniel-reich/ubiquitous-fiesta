
def tic_tac_toe(b):
  lists = [b[0], b[1], b[2],
           [b[0][0], b[1][0], b[2][0]],
           [b[0][1], b[1][1], b[2][1]],
           [b[0][2], b[1][2], b[2][2]],
           [b[0][0], b[1][1], b[2][2]],
           [b[0][2], b[1][1], b[2][0]]]
  for i in lists:
    if len(set(i)) == 1:
      return i[0]
  return "Draw"

