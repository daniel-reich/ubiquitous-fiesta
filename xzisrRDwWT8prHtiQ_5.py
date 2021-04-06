
from itertools import combinations
def difference_two(lst):
  return sorted(sorted([a, b]) for a, b in combinations(lst, 2) if abs(a-b)==2)

