
def tic_tac_toe(board):
  for i in board:
    if len(set(i))==1: return i[0]
  for i in list(zip(*board)):
    if len(set(i))==1: return i[0]
  if len({board[i][i] for i in range(3)})==1: return board[0][0]
  if len({board[i][2-i] for i in range(3)})==1: return board[0][2]
  return 'Draw'

