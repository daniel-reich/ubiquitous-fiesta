
def evl(o, a, b):
  return a*b if o=='*' else a/b if o=='/' else a+b if o=='+' else a-b
​
def postfix(exp):
  stack = []
  for x in exp.split():
    if x in '*/+-':
      x, stack = evl(x,*stack[-2:]), stack[:-2]
    stack.append(int(x))
  return int(stack[0])

