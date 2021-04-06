
def minesweeper_numbers(board):
  if not board: return board
  lr,lc = len(board),len(board[0])
  d = [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)]
  board = [[9 if i == 1 else 0 for i in row] for row in board]
  for i in range(lr):
    for j in range(lc):
      if board[i][j] == 0:
        board[i][j] = sum(board[i+x][j+y]==9 for x,y in d if 0<=i+x<lr and 0<=j+y<lc)
  return board

