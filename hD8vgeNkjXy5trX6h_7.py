
from itertools import combinations
def combo(lst, n):
  return list(map(list, combinations(lst, n)))

