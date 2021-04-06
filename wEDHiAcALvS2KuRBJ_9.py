
class StackCalc:
​
  def __init__(self):
    self.stack = [0]
    
  def run(self, instructions):    
    instructionList = instructions.split()
    for val in instructionList:
      try:
        operation(self.stack, val)
      except ValueError:
        self.stack.append('Invalid instruction: ' + val)
        return
    
  def getValue(self):
    return self.stack[-1]
      
def operation(numberList, instruction):
  if instruction == '+':
    a = numberList.pop()
    b = numberList.pop()
    numberList.append(a+b)
  elif instruction == '-':
    a = numberList.pop()
    b = numberList.pop()
    numberList.append(a-b)
  elif instruction == '*':
    a = numberList.pop()
    b = numberList.pop()
    numberList.append(a*b)
  elif instruction == '/':
    a = numberList.pop()
    b = numberList.pop()
    numberList.append(a/b)
  elif instruction == 'DUP':
    numberList.append(numberList[-1])
  elif instruction == 'POP':
    numberList.pop()
  elif instruction.isdigit():
    numberList.append(int(instruction))
  else:
    raise ValueError('Not a valid instruction')

