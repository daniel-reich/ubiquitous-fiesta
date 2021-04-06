
def boolean_and(lst):
  return all(lst)
​
def boolean_or(lst):
  return any(lst)
​
def boolean_xor(lst):
  from functools import reduce
  return reduce(lambda x, y: x^y, lst)

