
import functools as f
def get_products(lst):
  p = lambda a,b : a*b
  return [f.reduce(p,[n for j,n in enumerate(lst) if j!=i]) \
    for i in range(len(lst))]

