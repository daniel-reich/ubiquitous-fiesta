
from itertools import groupby
​
def group_seats(lst, n):
  result = 0
  for item in lst:
    for key, val in groupby(item):
      if not key:
        len_0 = len(list(val))
        if len_0 == n:
          result += 1
        elif len_0 > n:
          result += 2
  return result

