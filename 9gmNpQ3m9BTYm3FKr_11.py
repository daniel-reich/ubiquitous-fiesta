
from itertools import combinations 
def lucky_seven(lst):
  if len(lst) < 3:
    return False
  return any(a+b+c == 7 for a, b, c in list(combinations(lst,3)))

