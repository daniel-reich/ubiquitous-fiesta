
def knight(b, i, j):
  if i > 1:
    if j >0:
      if b[i-2][j-1] == 1:
        return True
    if j < len(b[i])-1:
      if b[i-2][j+1] == 1:
        return True
  if i < len(b)-2:
    if j >0:
      if b[i+2][j-1] == 1:
        return True
    if j < len(b[i])-1:
      if b[i+2][j+1] == 1:
        return True
  if i > 0:
    if j >1:
      if b[i-1][j-2] == 1:
        return True
    if j < len(b[i])-2:
      if b[i-1][j+2] == 1:
        return True
  if i < len(b)-1:
    if j >1:
      if b[i+1][j-2] == 1:
        return True
    if j < len(b[i])-2:
      if b[i+1][j+2] == 1:
        return True
def cannot_capture(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 1:
        if knight(board,i,j):
          return False
  return True

