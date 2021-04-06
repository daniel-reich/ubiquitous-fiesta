
class Stack:
  
  def __init__(self):
    self.stack = []
  
  def interact(self, item):
    try:
      i = int(item)
      self.stack.append(i)
  #   print(self.stack, i)
    except ValueError:
      try:
        n1 = self.stack[0]
        n2 = self.stack[1]
        
        newnum = eval('{}{}{}'.format(n1,item,n2))
        self.stack.pop(0)
        self.stack.pop(0)
        self.stack = [newnum] + self.stack
      except IndexError:
        return False
      print(self.stack, item, 18*3)
      return True
  
  def answer(self):
    
    return self.stack[0]
​
def post_fix(expr):
​
  s = Stack()
  
  for item in expr.split():
    s.interact(item)
  
  return s.answer()

