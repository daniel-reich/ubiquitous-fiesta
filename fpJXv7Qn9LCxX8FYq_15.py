
def solve(eq):
  eq = eq.split()
  if '+' in eq:
      x = int(eq[-1]) - int(eq[2])
  else:
      x = int(eq[-1]) + int(eq[2])
  return x

