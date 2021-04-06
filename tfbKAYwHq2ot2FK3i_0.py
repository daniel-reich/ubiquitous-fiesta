
from math import e, factorial
​
def non_repeats(radix):
  return int(e*(radix-1) * factorial(radix-1))

