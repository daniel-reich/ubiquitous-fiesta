
def postfix(expression):
  expression = expression.split(" ")
  calc = []
  for i in expression:
    if i.isdigit(): calc.append((i))
    else:
      a, b = calc.pop(), calc.pop()
      calc.append(eval("{}{}{}".format(b,i,a)))
  return calc[0]

