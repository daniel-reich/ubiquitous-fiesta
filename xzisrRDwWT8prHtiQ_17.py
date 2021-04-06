
from itertools import combinations as C
def difference_two(lst):
  return sorted([sorted(x) for x in C(lst, 2) if abs(x[0]-x[1])==2], key=lambda x:x[0])

