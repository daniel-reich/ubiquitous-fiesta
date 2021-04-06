
def solve(a, b):
  if a-b==0 and b-3*a+4==0:
    return "Any number"
  elif a-b==0 and b-3*a+4!=0:
    return "No solution"
  else:
    return round((b-3*a+4)/(a-b),3)

