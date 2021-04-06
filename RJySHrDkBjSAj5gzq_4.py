
from numpy import prod
​
def nespers(lst):
  return fact(len(lst)) * prod([nespers(i) for i in lst if type(i) is list])
​
def fact(n):
  return 1 if n < 2 else n * fact(n-1)

