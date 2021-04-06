
def solve(a, b):
  if b==1:
    return "Any number"
  elif a==1:
    return "No solution"
  return round((b-1)/(a-1),3)

