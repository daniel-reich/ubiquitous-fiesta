
def eval_algebra(eq):
  (a,b),(c,d) = map(eval_coef,eq.split(' = '))
  return (d-b)/(a-c)
  
def eval_coef(expr):
  a = b = 0
  op = 1
  for x in expr.split():
    if x == '-' : op = -1
    elif x == '+' : op = 1
    elif x[-1] == 'x': a += op * int(x[:-1] or 1)
    else: b += op * int(x)
  return (a,b)

