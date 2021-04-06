
def equal(a, b, c): 
  if a == b:
    return 3 if a == c else 2
  elif a == c: 
    return 2 
  elif b == c:
    return 2 
  return 0

