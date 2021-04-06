
from heapq import heapify, heappop, heappush
from itertools import product
​
def moves(the_map, x, y):
    neigh = []
    h = len(the_map)
    w = len(the_map[0])
    for dx, dy in product([-1, 0, 1], repeat=2):
        if dx == 0 and dy == 0:
            continue
        x2 = x + dx
        y2 = y + dy
        if x2 < 0 or y2 < 0 or x2 >= w or y2 >= h:
            continue
        if the_map[y2][x2] != 't':
            neigh.append((x2, y2)), 
    return neigh
​
def get_path_length(world, width, height):
  vals = world.split(',')
  w = [''.join(vals[width*r:(r+1)*width]) for r in range(height)]
  s = vals.index('m')
  start = (s % width, s//height)
  
  Q = []
  dists = {start: 0,}
  heappush(Q, (0, start))
​
  while Q:
      d, u = heappop(Q)
      if w[u[1]][u[0]] == 'h':
          return d
      for v in moves(w, *u):
          d2 = d + 1
          if v in dists:
            continue
          dists[v] = d2
          heappush(Q, (d2, v))
  return -1

