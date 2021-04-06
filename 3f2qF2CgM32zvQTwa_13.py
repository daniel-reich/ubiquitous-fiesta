
def format_math(expr):
  if 'x' in expr:
    res=eval(expr.replace('x', '*'))
  else:
    res=int(eval(expr))
  return (expr + ' = ' + str(res))

