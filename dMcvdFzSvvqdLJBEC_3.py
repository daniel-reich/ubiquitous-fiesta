
from math import factorial
def num_of_days(cost, savings, start):
  #money needed:
  cost -= savings
  #formula: f(n+1) = f(n) + 7; week 1: f(n) = start*n + factorial(n,2)
  days = 0
  if cost <= 0:
    return days
  elif cost - (7 * start + 21) <= 0:
    return 1 + num_of_days(cost-start,0,start+1)
  else:
    return 7 + num_of_days(cost - (7*start+21), 0, start + 1)

