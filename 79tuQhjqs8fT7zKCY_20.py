
def postfix(expr):
  expr = expr.split(' ')
  values = []
  
  for x in expr:
    if x == '+':
      values.append(values.pop(-2) + values.pop())
    elif x == '-':
      values.append(values.pop(-2) - values.pop())
    elif x == '*':
      values.append(values.pop(-2) * values.pop())
    elif x == '/':
      values.append(values.pop(-2) / values.pop())
    else:
      values.append(int(x))
    
  return values[0]

