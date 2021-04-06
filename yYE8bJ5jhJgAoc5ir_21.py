
from functools import reduce
from operator import mul
​
def bugger(number, count=0):
  if number < 10:
      return count
​
  new_number = reduce(mul, map(int, str(number)))
  return bugger(new_number, count + 1)

