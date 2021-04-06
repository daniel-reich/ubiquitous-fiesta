
def solve(eq):
  eq = eq.split()
  op = '+' if eq[1] == '-' else '-'
  return eval(eq[4] + op + eq[2])

