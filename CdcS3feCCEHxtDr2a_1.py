
from itertools import permutations
​
def clear_ordering(lst):
  for p in permutations(lst):
    if all(p[i][1] == p[i+1][0] for i in range(len(p) - 1)):
      return True
  return False

