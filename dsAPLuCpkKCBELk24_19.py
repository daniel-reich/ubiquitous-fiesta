
def get_products(lst):
  from functools import reduce 
  prod = []
  for i in range(len(lst)):
    tmp = lst.copy()
    tmp[i] = 1
    prod.append(reduce((lambda x, y: x * y), tmp))
  return prod

