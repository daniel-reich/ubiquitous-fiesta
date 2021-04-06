
def pos_add(x, y):
  return(x[0] + y[0], x[1] + y[1])
def in_bounds(p):
  return p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9
​
knight_moves = [(1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2, -1)]
​
def knight_bfs(a, b, c, d):
  p0 = (a, b)
  pf = (c, d)
  bfs_queue  = [p0]
  dist_map = {p0 : 0}
  
  def bfs_visit(p):
    for np in filter(in_bounds, [pos_add(p, m) for m in knight_moves]):
      if np not in dist_map:
        dist_map[np] = dist_map[p] + 1
        bfs_queue.append(np)
  
  while (pf not in dist_map) and (len(bfs_queue) > 0):
    bfs_visit(bfs_queue.pop(0))
  
  return dist_map.get(pf, None)

