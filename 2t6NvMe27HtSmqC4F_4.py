
def boolean_and(lst):
  if False in lst:
    return False
  return True
​
def boolean_or(lst):
  if True in lst:
    return True
  return False
​
def boolean_xor(lst):
  if lst.count(True)%2 == 0:
    return False
  return True

