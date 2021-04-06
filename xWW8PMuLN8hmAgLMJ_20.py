
def postfix(expr):
  exps, stack = expr.split(), []
  for index in range(len(exps)):
    op = exps[index]
    if op == '+':
      stack.append(stack.pop() + stack.pop())
    elif op == '-':
      stack.append(-stack.pop() + stack.pop())
    elif op == '*':
      stack.append(stack.pop() * stack.pop())
    elif op == '/':
      stack.append(stack.pop(-2) / stack.pop())
    else:
      stack.append(int(op))
  return stack[0]

