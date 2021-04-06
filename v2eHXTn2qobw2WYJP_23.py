
def minesweeper_numbers(board):
  pos = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y]
  neighbors = [[0 for c in r] for r in board]
  for i, r in enumerate(board):
    for j, c in enumerate(r):
      s = 0
      for x, y in pos:
        if 0 <= i+x < len(board) and 0 <= j+y < len(board[0]):
          s += board[i+x][j+y]
      neighbors[i][j] = 9 if board[i][j] else s
  return neighbors

