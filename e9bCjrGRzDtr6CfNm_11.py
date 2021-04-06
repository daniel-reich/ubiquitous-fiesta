
def solve(a, b):
  return "No solution" if b-3*a+4!=0 and a==b else "Any number" if a==b \
    else round((b-3*a+4)/(a-b),3)

