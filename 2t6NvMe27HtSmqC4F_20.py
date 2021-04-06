
def boolean_and(lst):
  return False not in lst
​
def boolean_or(lst):
  return True in lst
​
def boolean_xor(lst):
  return (len(lst)-lst.count(True))%2==1

