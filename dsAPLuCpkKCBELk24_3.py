
import operator, functools
​
def get_products(lst):
  return [functools.reduce(operator.mul, lst[0:i]+lst[i+1:len(lst)]) for i in range(len(lst))]

