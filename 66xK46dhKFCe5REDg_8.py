
def x_and_o(board):
  board = [row.split("|") for row in board]
  blanks = [[i,j] for i in [0,1,2] for j in [0,1,2] if board[i][j]==" "]
  for [i,j] in blanks:
    if [board[i][k] for k in [0,1,2]].count("X") == 2: return [i+1,j+1]
    if [board[k][j] for k in [0,1,2]].count("X") == 2: return [i+1,j+1]
    if i==j and [board[k][k] for k in [0,1,2]].count("X") == 2: return [i+1,j+1]
    if i+j==2 and [board[k][2-k] for k in [0,1,2]].count("X")==2: return [i+1,j+1]
  return False

