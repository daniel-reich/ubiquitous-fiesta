
from numpy import prod
from math import factorial
def nespers(lst):
  return factorial(len(lst))*prod([nespers(l) for l in lst if type(l) is list])

