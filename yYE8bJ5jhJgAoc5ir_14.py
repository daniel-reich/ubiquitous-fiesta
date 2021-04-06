
from functools import reduce
from operator import mul
count = 0
def bugger(num, count=0):
  if num < 10:
    return count
  new_number = reduce(mul, map(int, str(num)))
  
  return bugger(new_number, count+1)

