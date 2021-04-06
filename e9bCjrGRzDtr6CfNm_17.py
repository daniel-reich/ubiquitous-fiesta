
def solve(a, b):
  if b-3*a+4 == 0:
    return "Any number"
  elif a==b:
    return "No solution"
  else:
    return round((b-3*a+4)/(a-b),3)

