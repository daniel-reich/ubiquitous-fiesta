
import math
def fact_of_fact(n):
  result = 1
  for i in range(1, n+1):
    result *= math.factorial(i)
  return result

