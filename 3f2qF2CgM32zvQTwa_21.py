
def format_math(expr):
  exp = ['/', '+', '-', 'x']
  oper = ''
  expr = expr.strip()
  answer = 0
  for e in expr:
    if e in exp:
      oper = e
  num = expr.split(oper)
  if oper == '+':
    answer = expr + ' = ' + str(int(int(num[0]) + int(num[1])))
  elif oper == '-':
    answer = expr + ' = ' + str(int(int(num[0]) - int(num[1])))
  elif oper == 'x':
    answer = expr + ' = ' + str(int(int(num[0]) * int(num[1])))
  else:
    answer = expr + ' = ' + str(int(int(num[0]) / int(num[1])))
  return(answer)

