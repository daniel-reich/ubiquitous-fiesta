
def solve(eq):
  eq = eq.split(' ')
  eq[0], eq[-1] = eq[-1], eq[0]
  if eq[1] == '+':
    eq[1] = '-'
  else:
    eq[1] = '+'
  return eval(''.join(el for el in eq[:3]))

