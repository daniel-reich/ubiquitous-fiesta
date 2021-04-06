
def who_won(board):
  for s in 'OX':
    if [s]*3 in board:
      return s
    if [s]*3 in [[board[i][i] for i in range(3)], [board[2-i][i] for i in range(3)]]:
      return s
    if (s,)*3 in list(zip(*board)):
      return s

