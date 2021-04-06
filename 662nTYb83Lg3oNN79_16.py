
from itertools import permutations as P
def is_parallelogram(lst):
  return any(x[0][0]+x[1][0]==x[2][0]+x[3][0] and x[0][1]+x[1][1]==x[2][1]+x[3][1] for x in P(lst))

