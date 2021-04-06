
from numpy import prod
​
def accumulating_product(lst):
  return [prod(lst[:i+1]) for i in range(len(lst))]

