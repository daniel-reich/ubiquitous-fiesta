
def check_board(col, row):
  row=8-row
  board=[[0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],]
  a='abcdefgh'
  col=a.index(col)
  board[row]=[1]*8
  for i in range(len(board)):
    board[i][col]=1
  board[row][col]=0
  for i in range(8):
    if row+i<8 and col+i<8: board[row+i][col+i]=1
  for i in range(8):
    if row-i>=0 and col+i<8: board[row-i][col+i]=1
  for i in range(8):
    if row+i<8 and col-i>=0: board[row+i][col-i]=1
  for i in range(8):
    if row-i>=0 and col-i>=0: board[row-i][col-i]=1
  board[row][col]=0
  print((col+1,row+1))
  for i in board:
    print(i)
  return board

