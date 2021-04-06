
def solve(eq):
  eq = eq.replace(" ", "")
  x,y = eq.split("=")
  return int(y) + int(x[2::]) if x[1] == "-" else  int(y) - int(x[2::])

