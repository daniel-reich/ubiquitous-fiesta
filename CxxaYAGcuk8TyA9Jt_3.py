
def checkBalance(expression):
  stack = ''
  for i,s in enumerate(expression):
    if s in '{(': stack+= s
    if s == ')':
      if stack and stack[-1] == '(': stack = stack[:-1]
      else: return i
    if s == '}':
      if stack and stack[-1] == '{': stack = stack[:-1]
      else: return i
  return i+1 if stack else -1

