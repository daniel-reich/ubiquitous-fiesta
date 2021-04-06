
def format_math(expr):
  return '{} = {}'.format(expr,eval(expr.replace('x','*').replace('/','//')))

