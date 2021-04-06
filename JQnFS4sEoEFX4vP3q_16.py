
import itertools
import numpy
def product_pair(lst, k):
  if k<=len(lst):
    a=sorted([numpy.prod(i) for i in itertools.combinations(lst,k)])
    return (a[0],a[-1])

