
def x_and_o(board):
  board = [i.split('|') for i in board]
  for i in range(len(board)):
    if board[i].count("X")==2 and board[i].count(" ")==1:
      return [i+1,board[i].index(' ')+1]
  col = [[i[j] for i in board] for j in range(3)]
  for i in range(len(col)):
    if col[i].count("X")==2 and col[i].count(" ")==1:
      return [col[i].index(' ')+1,i+1]
  if board[1][1]==' ' and ((board[0][0]=='X' and board[2][2]=='X') or (board[0][2]=='X' and board[2][0]=='X')):
    return [2,2]
  if board[0][0]==' ' and board[1][1]=='X' and board[2][2]=='X':
    return [1,1]
  if board[0][0]=='X' and board[1][1]=='X' and board[2][2]==' ':
    return [3,3]
  if board[0][2]==' ' and board[1][1]=='X' and board[2][0]=='X':
    return [1,3]
  if board[0][2]=='X' and board[1][1]=='X' and board[2][0]==' ':
    return [3,1]
  return False

