
def format_math(expr):
  new = ''
  if 'x' in expr:
    new = expr.replace('x','*')
  else:
    new = expr
    
  answer = int(eval(new))
  
  return "{} = {}".format(expr, answer)

