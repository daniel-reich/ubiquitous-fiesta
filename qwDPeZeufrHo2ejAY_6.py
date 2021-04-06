
def eval_algebra(eq):
  eq = eq.split()
  a, b, c = eq[::2] if eq[1] == '+' else eq[::2][::-1]
  if a == 'x':
    return int(c) - int(b)
  if b == 'x':
    return int(c) - int(a)
  if c == 'x':
    return int(a) + int(b)

