
def smallest(digits, value):
  check = 0
  
  while len(str(check)) != digits:
    check += value
  
  return check

