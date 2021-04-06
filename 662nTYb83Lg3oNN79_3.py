
from itertools import permutations as p
def is_parallelogram(lst):
  slope = lambda p1, p2: abs(p1[0]-p2[0])/abs(p1[1]-p2[1])
  for A, B, C, D in p(lst,4):
    try:
      if slope(A, B) == slope(C, D) and slope(A, D) == slope(B, C):
        return True
    except:
      pass
  return False

