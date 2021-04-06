
from functools import reduce
def persistence(num):
  cnt = 0
  while num >= 10:
    if num >= 10:
      num = reduce((lambda x, y: x * y), [int(i) for i in list(str(num))])
      cnt += 1
  return cnt

