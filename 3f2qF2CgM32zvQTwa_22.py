
def format_math(expr):
  return expr + ' = ' + str(eval(expr.replace('x', '*').replace('/', '//')))

