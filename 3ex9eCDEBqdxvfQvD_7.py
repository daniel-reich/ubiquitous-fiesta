
def are_true(a,b):
  if a and b:
    return "both"
  elif a and not b:
    return "first"
  elif b and not a:
    return "second"
  else:
    return "neither"

