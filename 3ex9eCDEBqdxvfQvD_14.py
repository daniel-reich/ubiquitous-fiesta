
def are_true(a, b):
  if a and b is True :
    return "both"
  elif a is True:
    return "first"
  elif b is True:
    return "second"
  return "neither"        
​
print(are_true(False, False))

