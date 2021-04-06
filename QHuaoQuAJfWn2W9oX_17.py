
import pprint
​
def check_board(col, row):
  row, col = ord(col)-97,8-row
  
  board = []
  for j in range(8):
    r = []
    for i in range(8):
​
      if i-row==j-col or i-col==-j+row or i==row or j == col:
        r.append(1)
      else:
        r.append(0)
    board.append(r)
  board[col][row]=0
  
  return board

