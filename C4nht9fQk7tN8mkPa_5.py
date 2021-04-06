
def cannot_capture(board):
  def check(a,b):
    if a > -1 and a < 8 and b > -1 and b < 8:
      if board[a][b]==1:
        return True
    return False
  moves = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
  for i in range (64):
    if check(i//8,i%8):
      for j in moves:
        if check(i//8+j[0],i%8+j[1]):
          return False
  return True

