
def solve(a,b):
  if a==1 and b==1:
    return "Any number"
  try:
    return round((b-1)/(a-1),3)
  except:
    return "No solution"

