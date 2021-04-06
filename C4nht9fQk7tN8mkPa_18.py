
def cannot_capture(board):
  for i in range(7):
    for j in range(8):
      if(i>5):
        if(j<=1):
          if(board[i][j]*board[i+1][j+2]==1):
            return False
        elif(j>5):
          if(board[i][j]*board[i+1][j-2]==1):
            return False
        else:
          if(board[i][j]*board[i+1][j+2]==1 or board[i][j]*board[i+1][j-2]==1):
            return False
      else:
        if(j<=1):
          if(board[i][j]*board[i+1][j+2]==1 or board[i][j]*board[i+2][j+1]==1):
            return False
        elif(j>5):
          if(board[i][j]*board[i+1][j-2]==1or board[i][j]*board[i+2][j-1]==1):
            return False
        else:
          if(board[i][j]*board[i+1][j+2]==1 or board[i][j]*board[i+1][j-2]==1 or board[i][j]*board[i+2][j+1]==1 or board[i][j]*board[i+2][j-1]==1):
            return False
  return True

