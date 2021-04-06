
import numpy
def accumulating_product(lst):
  return [numpy.prod(lst[0: (i+1)]) for i in range(len(lst))]

