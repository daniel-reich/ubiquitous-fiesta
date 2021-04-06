
from math import sqrt
​
def standard_deviation(lst):
  mean = sum(lst) / len(lst)
  return round(sqrt(sum(abs(n - mean)**2 for n in lst) / len(lst)), 2)

