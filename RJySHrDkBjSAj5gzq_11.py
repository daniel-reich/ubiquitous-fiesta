
from functools import reduce
from math import factorial
from operator import mul
def nespers(lst):
  if isinstance(lst, list):
    return factorial(len(lst)) * reduce(mul, map(nespers, lst), 1)
  else:
    return 1

