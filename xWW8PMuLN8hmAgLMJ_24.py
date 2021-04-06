
def postfix(expression):
  stack = []
  for op in expression.split():
    if op in '+-*/':
      a = stack.pop()
      b = stack.pop()
      stack.append(eval('{}{}{}'.format(b, op, a)))
    else:
      stack.append(int(op))
  return stack[0]

