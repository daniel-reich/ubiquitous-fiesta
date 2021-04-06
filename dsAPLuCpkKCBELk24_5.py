
from functools import reduce
from operator import mul
​
def get_products(lst):
  i=0
  prods = []
  while i<len(lst):
    c = lst[i]
    t = [n for n in lst if n!=c]
    prods.append(reduce(mul, t))
    i+=1
  return prods

