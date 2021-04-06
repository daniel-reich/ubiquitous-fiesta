
def cannot_capture(board):
  for i in range(8):
    for j in range(8):
      if board[i][j] == 1:
        if helper(board,i,j):
          return False
  return True
      
def helper(board,row,col):
  rslt = [chk(board,row+2,col+1),chk(board,row+2,col-1),
          chk(board,row-2,col+1),chk(board,row-2,col-1),
          chk(board,row+1,col+2),chk(board,row+1,col-2),
          chk(board,row-1,col+2),chk(board,row-1,col-2)]
  return any(rslt)
  
def chk(board,row,col):
  if(row < 0 or col < 0 or row > 7 or col > 7):
    return False
  else:
    return board[row][col] == 1

