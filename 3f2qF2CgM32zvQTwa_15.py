
def format_math(expr):
  return ' '.join(expr.split()) + ' = ' + str(int(eval(expr.replace('x','*'))))

