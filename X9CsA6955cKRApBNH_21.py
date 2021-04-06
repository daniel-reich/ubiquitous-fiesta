
from itertools import groupby
​
def longest_run(lst):
  inc = [b == a + 1 for a, b in zip(lst, lst[1:])]
  dec = [b == a - 1 for a, b in zip(lst, lst[1:])]
  return max([sum(g) for _, g in groupby(inc)] + [sum(g) for _, g in groupby(dec)]) + 1

