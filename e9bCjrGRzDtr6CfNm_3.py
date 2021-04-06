
def solve(a, b):
  return round((-3*a+4+b)/(a-b),3) if a!=b else "No solution" if -b!=-3*a+4 else "Any number"

