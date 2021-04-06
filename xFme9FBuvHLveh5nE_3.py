
from itertools import groupby
​
def is_zygodrome(num):
  return min(len(list(g)) for k, g in groupby(str(num))) >= 2

