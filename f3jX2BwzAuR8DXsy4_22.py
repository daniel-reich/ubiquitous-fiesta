
import math
from functools import reduce
def fact_of_fact(n):
  m = [math.factorial(i) for i in list(range(1, n+1))]
  return reduce((lambda x, y: x * y), m)

