
def prefix(exp):
  exp=exp.replace('/', '//')
  A=exp.split()
  stack=[]
  for x in A[::-1]:
    if x not in {'+', '-', '*', '//'}:
      stack.append(x)
    else:
      stack.append(str(eval(stack.pop()+x+stack.pop())))
  return int(stack[0])

