
from itertools import combinations as C
def check_sum(lst, n):
  return any(sum(x)==n for x in C(lst,2))

