
class StackCalc:
​
  def __init__(self):
    self.stack=[]
    
  def run(self, instructions):
    self.stack=[]
    instructions=instructions.split()
    for i in instructions:
      if i in '+-*/':
        self.stack+=[eval(str(self.stack.pop())+i+str(self.stack.pop()))]
      elif i == 'DUP':
        self.stack+=[self.stack[-1]]
      elif i == 'POP':
        self.stack.pop()
      elif all([j.isdigit() for j in i.split('.')]):
        self.stack+=[eval(i)]
      else:
        self.stack=['Invalid instruction: '+i]
        break
​
  def getValue(self):
    return self.stack[-1] if self.stack else 0

