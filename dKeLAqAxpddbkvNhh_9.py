
from itertools import groupby 
​
def group_seats(lst, n):
  total = 0
  for i in lst:
    total += groupS(i, n)
  return total
​
def groupS(l,n):
  stotal = 0
  l1 = [list(i).count(0) for g,i in groupby(l) if g == 0]
  for s in l1:
    if s >= n:
      stotal += (s-n) +1
  return stotal

