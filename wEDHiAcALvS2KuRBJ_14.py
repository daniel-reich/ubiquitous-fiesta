
class StackCalc:
  def __init__(self):
    pass
  def run(self, instructions):
    self.instructions = list(self.process_instructions(instructions))
    self.stack = [0]
    for i in self.instructions:
      if isinstance(i, int):
        self.stack.append(i)
      elif i == '':
        self.stack.append(0)
        break
      elif i == '+':
        self.stack.append(self.stack.pop()+self.stack.pop())
      elif i == '-':
        self.stack.append(self.stack.pop()-self.stack.pop())
      elif i == '*':
        self.stack.append(self.stack.pop()*self.stack.pop())
      elif i == '/':
        self.stack.append(self.stack.pop()/self.stack.pop())
      elif i == 'DUP':
        self.stack.append(self.stack[-1])
      elif i == 'POP':
        self.stack.pop()
      else:       
        self.stack.append('Invalid instruction: {}'.format(i))
        break
​
  def getValue(self):
    if self.stack != []:
      return self.stack[-1]
    else:
      return 0
  
  @staticmethod
  def process_instructions(string):
    for i in string.split(' '):
      if i.isnumeric():
        yield int(i)
      else:
        yield i

