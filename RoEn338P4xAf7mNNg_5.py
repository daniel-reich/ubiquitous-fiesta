
from functools import reduce
def shortest_path(lst):
  p = sorted([(lst[r][c], r, c) for r in range(len(lst)) for c in range(len(lst[0])) if lst[r][c] > '0'])
  v, h = reduce(lambda m,i: (m[0]+abs(p[i][1]-p[i-1][1]), m[1]+abs(p[i][2]-p[i-1][2])), range(1, len(p)), (0,0))
  return v + h

