
from itertools import combinations as C
def lucky_seven(lst):
  if len(lst)<3:
    return False
  else:
    return any(sum(x)==7 for x in C(lst,3))

