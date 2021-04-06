
def solve(eq):
  eq = eq.split()
  pm = {'+':'-','-':'+'}
  return eval(eq[-1]+pm[eq[1]]+eq[2])

