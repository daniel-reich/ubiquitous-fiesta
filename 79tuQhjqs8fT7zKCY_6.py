
import operator
ops = { '+':operator.add, 
        '-':operator.sub, 
        '/':operator.floordiv, 
        '*':operator.mul}
​
def postfix(expr):
  stack  = []
  for term in expr.split():
    if term in ops:
      a2, a1 = stack.pop(), stack.pop()
      stack.append(ops[term](a1, a2))
    else:
      stack.append(int(term))
  return stack.pop()

