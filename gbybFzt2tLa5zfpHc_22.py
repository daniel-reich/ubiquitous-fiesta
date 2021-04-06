
from itertools import combinations
​
def three_sum(lst):
  result = []
  for i in combinations(lst, 3):
    if sum(i) == 0:
      tmp = list(i)
      if tmp not in result:
        result.append(tmp)
  return result

