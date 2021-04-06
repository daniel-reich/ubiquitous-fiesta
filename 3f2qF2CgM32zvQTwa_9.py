
def format_math(expr):
  lst = expr.split(' ')
  if lst[1] == '+':
   res = eval(lst[0]+'+'+lst[-1])
  elif lst[1] == '-':
    res = eval(lst[0]+'-'+lst[-1])
  elif lst[1] == 'x':
    res = eval(lst[0]+'*'+lst[-1])
  elif lst[1] == '/':
    res = int(eval(lst[0]+'/'+lst[-1]))
  return expr + ' = ' + str(res)

