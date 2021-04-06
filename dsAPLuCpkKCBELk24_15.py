
import functools
def get_products(l):
  return [functools.reduce(lambda x,y:x*y,l[:i]+l[i+1:]) for i in range(len(l))]

