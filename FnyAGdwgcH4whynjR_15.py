
from itertools import combinations
def get_subsets(lst, n):
  o = []
  for length in range(1, len(lst)+1):
    for combi in combinations(lst, length):
      if sum(combi) == n:
        combi = sorted(combi)
        if combi not in o:
          o.append(combi)
  return o

