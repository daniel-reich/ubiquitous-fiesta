
import functools
​
def boolean_and(lst):
  return all(lst)
​
def boolean_or(lst):
  return any(lst)
​
def boolean_xor(lst):
  return functools.reduce(lambda a,b: a != b, lst)

