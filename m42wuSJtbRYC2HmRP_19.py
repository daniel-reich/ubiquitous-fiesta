
from math import log
​
def largest_exponential(lst):
  lst = [i[1] * log(i[0]) for i in lst]
  return lst.index(max(lst)) + 1

