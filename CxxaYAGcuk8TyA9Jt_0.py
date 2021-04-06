
def check_balance(expression):
  stack = []
  for i, c in enumerate(expression):
    if c in '({':
      stack.append(c)
    elif c in '})':
      if not stack: 
        return i
      ob = stack.pop()
      if (ob == '(' and c != ')') or (ob == '{' and c != '}'):
        return i
  return len(expression) if stack else -1

