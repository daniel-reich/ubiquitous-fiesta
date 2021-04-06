
from itertools import combinations
​
def three_sum(lst):
  arr = [i for i in combinations(lst, 3) if sum(i) == 0]
  return list(map(list, sorted(set(arr), key=arr.index)))

