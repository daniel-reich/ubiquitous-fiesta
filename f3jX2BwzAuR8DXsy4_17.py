
import math
from functools import reduce
​
def fact_of_fact(n):
  return reduce((lambda x,y: x*y),[math.factorial(x) for x in range(1,n+1)])

