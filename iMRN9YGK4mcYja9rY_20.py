
from numpy import prod
def accumulating_product(lst):
  return [prod(lst[:i]) for i in range(1, len(lst)+1)]

