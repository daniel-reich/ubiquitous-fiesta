
def solve(eq):
  x = eq.split(" ")
  if "+" in x:
    return int(x[4]) - int(x[2])
  else:
    return int(x[4]) + int(x[2])

