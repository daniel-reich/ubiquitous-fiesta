
def minesweeper_numbers(board):
  for i in range(len(board)):
    board[i] = [9 if j==1 else 0 for j in board[i]]
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j]==0:
        vert = (i>0 and board[i-1][j]==9)+(i<len(board)-1 and board[i+1][j]==9)
        hori = (j>0 and board[i][j-1]==9)+(j<len(board)-1 and board[i][j+1]==9)
        topd = (0 not in (i,j) and board[i-1][j-1]==9)+(len(board)-1 != j and i != 0 and board[i-1][j+1]==9)
        botd = (0 != j and len(board)-1 != i and board[i+1][j-1]==9)+(len(board)-1 not in (i,j) and board[i+1][j+1]==9)
        board[i][j] = vert+hori+topd+botd
  return board

