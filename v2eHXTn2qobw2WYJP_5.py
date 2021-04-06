
def minesweeper_numbers(board):
  def digit(i,j):
    if board[i][j] == 1:
      return 9
    total = 0
    for a,b in zip([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]):
      try:
        if min(a+i,b+j) >= 0:
          if board[a+i][b+j] == 1:
            total += 1
      except IndexError:
        pass
    return total
  return [[digit(i,j) for j in range(0,len(board[0]))] for i in range(0,len(board))]

