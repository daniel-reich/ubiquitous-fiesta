
def get_result(operator, stack, top):
  if operator == "+":
    return stack[top-1] + stack[top], 2
  elif operator == "-":
    return stack[top-1] - stack[top], 2
  elif operator == "*":
    return stack[top-1] * stack[top], 2
  elif operator == "/":
    return stack[top-2] / stack[top], 2
  else:
    return stack[top]
​
class stack():
  def __init__(self):
    self.data = []
    self.top = -1
​
  def push(self, item):
    self.top += 1
    if self.top < len(self.data):
      self.data[self.top] = item
    else:
      self.data.append(item)
      
  def pop(self):
    if self.top > -1:
      ret = self.data[self.top]
      self.top -= 1
      return ret
​
def push_result(operator, working):
  op2 = working.pop()
  op1 = working.pop()
  if operator == "+":
    working.push(op1 + op2)
  elif operator == "-":
    working.push(op1 - op2)
  elif operator == "*":
    working.push(op1 * op2)
  elif operator == "/":
    working.push(op1 / op2)
  
def postfix(expr):
  lexpr = expr.split()
  working = stack()
  
  for item in lexpr:
    if item in {"+", "-", "*", "/"}:
      push_result(item, working)
    else:
      working.push(int(item))
  return working.pop()

