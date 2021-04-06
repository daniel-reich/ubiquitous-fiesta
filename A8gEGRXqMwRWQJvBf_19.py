
def tic_tac_toe(board):
  for l in board:
    if l==l[:1]*3:return l[0]
  for l in zip(*board):
    if l==l[:1]*3:return l[0]
  for a in [board, board[::-1]]:
    if all(a[i][i]==a[2][2] for i in [0,1]):return a[0][0]
  return"Draw"

