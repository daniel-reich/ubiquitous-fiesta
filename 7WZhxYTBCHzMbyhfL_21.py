
def knight_bfs(a, b, c, d):
  moves = 0
  if a == c and b == d:
    return moves
  visited = [(a,b)]
  path = [[(a,b)]]
  coordinates = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
  def coords(i,j):
    return [(i+x[0],j+x[1]) for x in coordinates]
  while True:
    if any(item == (c,d) for item in path[0]):
      return moves
    else:
      path.append([])
      for item in path[0]:
        path[1].extend(list(filter(lambda x: not x in visited, coords(item[0],item[1]))))
      visited.extend(path[1])
      path.pop(0)
      moves += 1

