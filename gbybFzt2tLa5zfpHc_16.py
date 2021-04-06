
from itertools import combinations
def three_sum(lst):
  if len(lst) < 3: return []
  result, s3 = [], set()
  for combo in combinations(lst, 3):
    if sum(combo) == 0 and not combo in s3:
      result.append(list(combo))
      s3.add(combo)
  return result

