
import itertools
from functools import reduce
​
def product_pair(lst, k):
  if k > len(lst) or k < 1:
    return None
  elif k == 1:
    return (min(lst),max(lst))
  else:
    newlist = []
    product = 0
    for eachcombo in itertools.combinations(lst,k):
      product = reduce((lambda x,y: x*y),[x for x in eachcombo])
      newlist.append(product)
    return (min(newlist),max(newlist))

