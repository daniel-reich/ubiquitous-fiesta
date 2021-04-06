
# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
from itertools import combinations
import numpy as np
def does_brick_fit(a,b,c, w,h):
  for i in combinations([a,b,c], 2):
    if np.prod(i) <= w*h:
      return True
  return False

