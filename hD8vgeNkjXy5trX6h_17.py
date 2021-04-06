
from itertools import combinations
def combo(lst, n):
  NC = list(combinations(lst,n)) #new combo
  NL = [list(i) for i in NC]
  return NL

