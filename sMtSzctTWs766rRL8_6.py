
from operator import *
from functools import *
def magnitude(lst):
  return reduce(add, map(lambda x: x*x, lst), 0)**0.5

