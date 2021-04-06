
def distance(k, outer):
  return abs(outer - k)
​
def entry(k,i,j):
  return max(distance(k,i),distance(k,j))
​
def generate_rug(n):
  board = []
  k = n // 2
  for i in range(0,n):
    board.append([])
  for row in board:
    for i in range(0,n):
      row.append(0)
  for i in range(0,n):
    for j in range(0,n):
      board[i][j] = entry(k,i,j)
  return board

