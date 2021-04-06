
def eval_algebra(eq):
  a, b, c, d, e = eq.split()
  if e == 'x':
    return eval(a + b + c)
  if c == 'x':
    return eval(b + '(' + e + '-' + a + ')')
  return eval(e + '-(' + b + c + ')')

