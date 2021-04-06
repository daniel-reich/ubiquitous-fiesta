
def whoWon(board):
  for i in board:
    if i[0] == i[1] == i[2]:
      return i[0]
  for i in range(len(board)):
    if board[0][i] == board[1][i] == board[2][i]:
      return board[0][i]
  if board[0][0] == board[1][1] == board[2][2]:
    return board[0][0]
  if board[0][-1] == board[1][1] == board[2][0]:
    return board[0][-1]

