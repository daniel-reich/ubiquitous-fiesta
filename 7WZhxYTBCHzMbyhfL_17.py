
def valid(row, col):
  return 0 <= row < 8 and 0 <= col < 8
​
def create_edges(row, col):
  targets = []
  moves = [(1,2), (2,1)]
  for x in [-1, 1]:
    for y in[-1, 1]:
      for move in moves:
        ncol = col + move[0] * x
        nrow = row + move[1] * y
        if valid(nrow, ncol):
          targets.append((nrow, ncol))
  return targets
​
def lowest_unvisited(distance, visited):
  l_row = 0
  l_col = 0
  lowest = 8*8
  for row in range(8):
    for col in range(8):
      if visited[row][col]:
        continue
      if distance[row][col] is None:
        continue
      if distance[row][col] < lowest:
        lowest = distance[row][col]
        l_row = row
        l_col = col
  return l_row, l_col
​
def knight_bfs(a, b, c, d):
  a -= 1
  b -= 1
  c -= 1
  d -= 1
  edges = [[create_edges(r, c) for c in range(8)] for r in range(8)]
  visited = [[False for c in range(8)] for r in range(8)]
  distance = [[None for c in range(8)] for r in range(8)]
  distance[a][b] = 0
  while not visited[c][d]:
    row, col = lowest_unvisited(distance, visited)
    visited[row][col] = True
    ndistance = distance[row][col] + 1
    for (t_row, t_col) in edges[row][col]:
      if visited[t_row][t_col]:
        continue
      if distance[t_row][t_col] is None or distance[t_row][t_col] > ndistance:
        distance[t_row][t_col] = ndistance
  return distance[c][d]

