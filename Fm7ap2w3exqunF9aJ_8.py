
from itertools import groupby
def count_lone_ones(n):
  return sum(len(list(g))==1 and i=='1' for i,g in groupby(str(n)))

