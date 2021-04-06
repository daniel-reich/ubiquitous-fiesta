
def postfix(expression):
  commands = expression.replace('/', '//').split(' ')
  stack = []
  for i in commands:
    if i.isnumeric(): 
      stack.append(int(i))
    else:
      n1, n2 = stack.pop(), stack.pop()
      stack.append(eval('{}{}{}'.format(n2, i, n1)))
  return stack.pop()

