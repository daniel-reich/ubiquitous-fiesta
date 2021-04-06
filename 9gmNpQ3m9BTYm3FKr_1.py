
from itertools import combinations
​
def lucky_seven(r):
  return any(sum(x) == 7 for x in combinations(r, 3))

