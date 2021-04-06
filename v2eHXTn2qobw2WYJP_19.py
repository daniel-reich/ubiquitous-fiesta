
def minesweeper_numbers(board):
  ret = [0]*len(board)
  for i in range(len(ret)):
    ret[i]=[0]*len(board[0])
  for x in range(len(ret)):
    for y in range(len(ret[x])):
      if board[x][y]==1:
        ret[x][y] = 9
      else:
        temp = 0
        if x>0:
          temp+=board[x-1][y]
          if y>0: temp+=board[x-1][y-1]
          if y<len(ret[x])-1: temp+=board[x-1][y+1]
        if x<len(ret)-1:
          temp+=board[x+1][y]
          if y>0: temp+=board[x+1][y-1]
          if y<len(ret[x])-1: temp+=board[x+1][y+1]
        if y>0: temp+=board[x][y-1]
        if y<len(ret[x])-1: temp+=board[x][y+1]
        ret[x][y] = temp
  return ret

