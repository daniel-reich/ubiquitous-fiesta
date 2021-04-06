
from itertools import combinations
​
def lucky_seven(lst):
  l = list(combinations(lst, 3))
  for i in l:
    if sum(i) == 7:
      return True
  return False

