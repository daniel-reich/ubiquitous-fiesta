
def cannot_capture(board):
  for i in range(len(board)-1):
    for j in range(len(board[0])-2):
      if board[i][j] and board[i+1][j+2]:
        return False
  for i in range(len(board)-2):
    for j in range(len(board[0])-1):
      if board[i][j] and board[i+2][j+1]:
        return False
  for i in range(len(board)-1):
    for j in range(2,len(board[0])):
      if board[i][j] and board[i+1][j-2]:
        return False
  for i in range(len(board)-2):
    for j in range(1,len(board[0])):
      if board[i][j] and board[i+2][j-1]:
        return False
  return True

