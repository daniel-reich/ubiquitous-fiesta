
from itertools import combinations
​
def three_sum(lst):
  found = []
  for i in combinations(lst, 3):
    if sum(i) == 0 and list(i) not in found:
      found.append(list(i))
  return found

