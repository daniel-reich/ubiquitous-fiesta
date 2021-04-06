
import itertools
​
def lucky_seven(lst):
  return any(sum(i) == 7 for i in itertools.combinations(lst, 3))

