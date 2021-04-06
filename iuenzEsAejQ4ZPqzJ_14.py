
from math import log
​
def mystery_func(num):
  n = int(log(num,2))
  l = num - 2**n
  return int(n*'2' + str(l))

