
from math import ceil
def floyd(up_to = None, n_row = None):
  triangle = []
  current = 1
  if n_row is None:
    n_row = ceil((pow(8*up_to + 1,0.5) - 1) * 0.5)
  for i in range(1,n_row+1):
    triangle.append(list(range(current,current+i)))
    current+=i
  return triangle

