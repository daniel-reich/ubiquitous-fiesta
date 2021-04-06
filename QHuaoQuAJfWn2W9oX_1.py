
def check_board(c, r):
  r, c = 8-r,ord(c)-97
  board = {(i,j):0 for i in range(8) for j in range(8)}
  for k in range(1,8):
    for m,n in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
      if (r+k*m,c+k*n) in board:
        board[r+k*m,c+k*n] = 1
  return [[board[(i,j)]for j in range(8)]for i in range(8)]

