
import math
def fact_of_fact(n):
  if n==1:return 1
  return math.factorial(n)*fact_of_fact(n-1)

