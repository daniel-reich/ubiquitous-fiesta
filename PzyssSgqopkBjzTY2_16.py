
def can_exit(lst):
  if lst[0][0] == 1:
    return False
  m = len(lst)
  n = len(lst[0])
  visited = [[False for c in range(n)] for r in range(m)]
  to_visit = [(0,0)]
  
  def add_location(row, col):
    if not (0 <= row < m and 0 <= col < n):
      return
    if visited[row][col]:
      return
    if lst[row][col] == 1:
      return
    to_visit.append((row, col))
  
  while not visited[m-1][n-1]:
    if to_visit == []:
      return False
    (row, col) = to_visit.pop()
    visited[row][col] = True
    add_location(row + 1, col)
    add_location(row - 1, col)
    add_location(row, col + 1)
    add_location(row, col - 1)
  return True

