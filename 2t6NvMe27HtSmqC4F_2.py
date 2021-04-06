
def boolean_and(lst):
  return all(lst)
​
def boolean_or(lst):
  return any(lst)
​
def boolean_xor(lst):
  if lst.count(False)%2==1:
    return True
  return False

