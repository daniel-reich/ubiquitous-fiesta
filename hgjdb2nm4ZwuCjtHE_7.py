
def math_expr(expr):
  u = expr.split(' ')
  if len(u) == 1:
    if sum([(k in '+-*/%0123456789') for k in u[0]]) == 3:
        return True
  else:
    if sum([(k in '+-*/%0123456789') for k in u]) == 3:
      return True
  return False

