
from math import factorial
from functools import reduce
def fact_of_fact(n):
  return reduce(lambda x,y:x*y,(factorial(i) for i in range(1,n+1)))

