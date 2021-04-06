
def who_won(board):
  #vertical check
  for i in [0,1,2]:
    if board[i][0]==board[i][1]==board[i][2]:
      return board[i][0]
    if board[0][i]==board[1][i]==board[2][i]:
      return board[0][i]
  return board[1][1]
  #if board[1][1]==board[0][0]==board[2][2]:
  # return board[1][1]

