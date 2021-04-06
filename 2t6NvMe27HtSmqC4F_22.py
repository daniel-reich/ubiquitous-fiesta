
def boolean_and(lst):
  return not False in lst
​
def boolean_or(lst):
  return True in lst
  
​
def boolean_xor(lst):
  return lst.count(True) % 2 == 1

