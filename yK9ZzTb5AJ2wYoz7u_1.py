
from math import ceil,sqrt
def floyd(up_to = None, n_row = None):
  lst = []
  if up_to:
    n_row = ceil((-1 + sqrt(1+8*up_to))/2)
  start = lambda x: (x+1) * x // 2
  for i in range(1,n_row+1):
    lst.append(list(range(start(i-1)+1,start(i-1)+i+1)))
  return lst

