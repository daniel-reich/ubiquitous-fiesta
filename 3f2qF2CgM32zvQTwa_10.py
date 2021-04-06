
def format_math(expr):
  
  expr_list = expr.split(' ')
  
  if expr_list[1] == 'x':
    expr_list[1] = '*'
  
  return expr + ' = ' + str(int(eval( ' '.join(expr_list) ) ))

