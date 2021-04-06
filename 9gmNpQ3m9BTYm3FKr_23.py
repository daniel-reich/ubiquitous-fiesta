
from itertools import permutations
def lucky_seven(lst):
  return any(sum(s)==7 for s in permutations(lst, 3))

