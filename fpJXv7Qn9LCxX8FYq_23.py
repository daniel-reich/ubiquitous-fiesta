
def solve(eq):
  eq = eq.split()
  if eq[1] == '+':
    return int(eq[-1]) - int(eq[2])
    
  elif eq[1] == '-':
    return int(eq[-1]) + int(eq[2])

