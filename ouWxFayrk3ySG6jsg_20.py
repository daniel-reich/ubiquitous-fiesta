
def who_won(board):
  for i in board:
    l = []
    for j in i:
      l.append(j)
    if l[0] == l[1] and l[0] == l[2]:
      return l[0]
        
  if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
    return board[0][0]
  board.reverse()
  if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
    return board[0][0]
  if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
    return board[0][0]
  if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
    return board[0][1]
  if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
    return board[0][2]

