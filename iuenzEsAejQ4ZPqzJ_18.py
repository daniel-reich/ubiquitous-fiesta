
from math import log
def mystery_func(num):
  p = int(log(num,2))
  return int('2'* p  + str(num - 2**p))

