
def boolean_and(lst):
  return all(lst)
​
def boolean_or(lst):
  return any(lst)
​
def boolean_xor(lst):
  return lst.count(True) == 1 or lst.count(False) == 1

