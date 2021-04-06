
def postfix(expr):
  u, a = expr.split(' '), []
  for i in u:
    if i not in '+-*/':
      a.append(int(i))
    else:
      op2 = a.pop()
      op1 = a.pop()
      if i == '+':
        a.append(op1 + op2)
      elif i == '-':
        a.append(op1 - op2)
      elif i == '*':
        a.append(op1 * op2)
      else:
        a.append(op1 / op2)
  return a[-1]

