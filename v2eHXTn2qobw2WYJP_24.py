
nbrs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
​
def minesweeper_numbers(board):
  size = len(board)
  is_mine = lambda r, c: size>r>=0 and size>c>=0 and board[r][c]==1
  mines = lambda r, c: len(list(filter(bool, [is_mine(r+dr, c+dc) for dr, dc in nbrs])))
​
  return [[9 if board[r][c] == 1 else mines(r, c) for c in range(size)] for r in range(size)]

