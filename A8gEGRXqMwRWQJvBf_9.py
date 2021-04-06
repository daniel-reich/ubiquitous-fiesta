
def tic_tac_toe(board):
  for r in board:
    if len(set(r)) == 1: return r[0]
  for c in zip(*board):
    if len(set(c)) == 1: return c[0]
  if board[0][0] == board[1][1] == board[2][2]:
    return board[0][0]
  if board[0][2] == board[1][1] and board[2][0] == board[1][1]:
    return board[0][2]
  return "Draw"

