
def postfix(expr):
  stack = []
  for x in expr.split():
    if x.isdigit():
      stack.append(x)
    else:
      a, b = stack.pop(), stack.pop()
      stack.append(str(round(eval(b+x+a))))
  return int(stack.pop())

