
def minesweeper_numbers(board):
  if not board: return board
  m,n = len(board), len(board[0])
  ans = [row.copy() for row in board]
  
  for i in range(m):
    for j in range(n):
      if board[i][j]:
        ans[i][j] = 9
      else:
        for a,b in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,1),(-1,0),(-1,-1)]:
          x,y = i+a,j+b
          if 0<=x<m and 0<=y<m:
            ans[i][j] += board[x][y]
  return ans

