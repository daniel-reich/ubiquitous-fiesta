
from itertools import *
def does_brick_fit(a,b,c, w,h):
​
  brick = [a, b, c]
  hole = [w, h]
  v, b = hole 
  hole = v * b
  x = list(combinations(brick, 2))
​
  l = []
  for tup in x:
    z, i = tup 
    l.append(z * i)
​
  if hole in l:
    return(True)
  else:
    return(False)

