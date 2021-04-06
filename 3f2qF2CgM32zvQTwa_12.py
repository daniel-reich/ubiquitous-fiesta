
def format_math(expr):  
  listy = []
  for i in expr.split():
    if i == 'X' or i == 'x':
      listy.append('*')
    else:
      listy.append(i)
  return '{} = {}'.format(expr, int(eval(''.join(listy))))

