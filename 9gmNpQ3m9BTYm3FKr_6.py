
from itertools import combinations as cb
def lucky_seven(lst):
  return any(sum(x)==7 for x in cb(lst,3))

