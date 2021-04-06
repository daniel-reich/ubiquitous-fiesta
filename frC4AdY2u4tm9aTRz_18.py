
from math import sqrt
def standard_deviation(lst):
  mean = sum(lst)/len(lst)
  
  z = [(abs(mean-x))**2 for x in lst]
  f = sum(z)/len(lst)
  return round(sqrt(f),2)

