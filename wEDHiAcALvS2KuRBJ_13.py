
class StackCalc:
​
  def __init__(self):
    self.stack = [0]
    self._instructions_1 = ['DUP', 'POP']
    self._instructions_2 = ['+', '-', '*', '/']
​
  def run(self, instructions):
    for instruction in instructions.split():
    
      if instruction.isdigit():
        self.stack.append(int(instruction))
        continue
        
      if instruction in self._instructions_1:
        if len(self.stack) < 1:
          self.stack = ['Empty set encountered.']
          break
        elif instruction == 'DUP':
          self.stack.append(self.stack[-1])
        elif instruction == 'POP':
          self.stack.pop()
        continue
        
      if instruction in self._instructions_2:
        if len(self.stack) < 2:
          self.stack = ['Not enough elements in stack.']
          break
        a, b = self.stack.pop(), self.stack.pop()
        if instruction == '+':
          self.stack.append(a + b)
        elif instruction == '-':
          self.stack.append(a - b)
        elif instruction == '*':
          self.stack.append(a * b)
        elif instruction == '/':
          self.stack.append(a / b)
        continue
        
      if instruction != '': 
        self.stack = ["Invalid instruction: {}".format(instruction)]
        break
      
  def getValue(self):
    return self.stack[-1] if len(self.stack) > 0 else None

