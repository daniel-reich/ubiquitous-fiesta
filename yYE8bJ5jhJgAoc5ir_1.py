
from operator import *
from functools import *
def bugger(num):
  if num <= 9: return 0
  return 1 + bugger(reduce(mul, map(int, str(num))))

