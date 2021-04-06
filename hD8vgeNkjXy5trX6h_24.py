
from itertools import combinations
def combo(lst, n):
  return [list(i) for i in list(combinations(lst, n))]

