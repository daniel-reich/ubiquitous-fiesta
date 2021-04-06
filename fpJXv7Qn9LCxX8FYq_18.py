
def solve(eq):
  eq = eq.split()
  return int(eq[4]) - int(eq[2]) if eq[1] == '+' else int(eq[4]) + int(eq[2])

