
from functools import reduce
​
def prod(lst):
  return 1 if len(lst) == 0 else reduce(lambda x, y: x * y, lst)
​
def f(n):
  return 1 if n < 2 else n * f(n - 1)
  
def nespers(lst, level = 0):
  return f(len(lst)) * prod([nespers(e, level + 1) for e in lst if type(e) is list])

