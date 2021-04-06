
import math
import functools
def nespers(lst):
  product = math.factorial(len(lst))
  lst = list(filter(lambda x: isinstance(x,list) and len(x) > 1,lst))
  if len(lst) == 0:
    return product
  else:
    return product * functools.reduce(lambda x,y: x * y,list(map(lambda z: nespers(z),lst)))

