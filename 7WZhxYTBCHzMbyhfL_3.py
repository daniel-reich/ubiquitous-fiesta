
def knight_bfs(a, b, c, d):
  dist = {(a,b):0}
  moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
  board = {(i,j) for i in range(1,9) for j in range(1,9)}
  queue = [(a,b)]
  while queue:
    (k,l) = queue.pop(0)
    if (k,l) == (c,d): return dist[(k,l)]
    for (i,j) in moves:
      if (k+i,l+j) not in dist and (k+i,l+j) in board:
        dist[(k+i,l+j)] = dist[(k,l)]+1
        queue+= [(k+i,l+j)]

