
def postfix(expression):
  expression = expression.split()
  stack = []
  sp =- 1
  while(len(expression)>1):
    for i in expression:
      sp += 1
      stack.append(i)
      if str(stack[-1]) in "-+/*":
        op = str(stack[sp-2]) + str(stack[sp]) + str(stack[sp-1])
        for j in range(3):
          stack.pop(-1)
        stack.append(eval(op))
        sp -= 2 
    sp=-1
    expression = stack.copy()
    stack=[]
    
  return expression[0]

