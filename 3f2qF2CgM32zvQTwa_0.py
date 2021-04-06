
def format_math(expr):
  return '{} = {}'.format(expr, int(eval(expr.replace('x', '*'))))

