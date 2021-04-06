
from sys import setrecursionlimit
setrecursionlimit(100000000)
def digits_sum(start, stop):
  if start == stop:
      return sum(map(int, str(stop)))
  else:
      return sum(map(int, str(stop))) + digits_sum(start,stop-1)

