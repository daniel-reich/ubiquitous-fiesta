
from itertools import combinations
​
def lucky_seven(lst):
  return any(sum(subset) == 7 for subset in combinations(set(lst), 3))

