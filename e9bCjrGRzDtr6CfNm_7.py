
def solve(a, b):
  if not b-3*a+4: 
    return "Any number"
  elif not a-b:
    return "No solution"
  return round((b-3*a+4)/(a-b),3)

