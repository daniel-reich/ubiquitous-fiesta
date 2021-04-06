
def format_math(expr):
  v = eval(expr.replace('x','*').replace('/','//'))
  return '{} = {}'.format(expr, v)

