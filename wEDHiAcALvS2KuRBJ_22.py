
class StackCalc:
​
  def __init__(self):
    None
​
  def run(self, instructions):
    func, ndx = True, 1
    instructions = instructions.split()
​
    if not instructions:
      instructions += '0'
    elif instructions[0].isdigit() and len(instructions) > 1:
      for i in range(len(instructions)):
        if not instructions[i].isdigit():
          ndx = i
          break
​
    self.operands = instructions[:ndx]
    self.operators = instructions[ndx:]
​
    if any(val.isalpha() for val in self.operands):
      self.operands = ['Invalid instruction: %s' % self.operands[0]]
      func = False
    else:
      self.operands = [int(x) for x in self.operands]
​
    if func:
      for op in self.operators:
        if op == '+':
          self.operands.append(self.operands.pop() + self.operands.pop())
        elif op == '-':
          self.operands.append(self.operands.pop() - self.operands.pop())
        elif op == '*':
          self.operands.append(self.operands.pop() * self.operands.pop())
        elif op == '/':
          self.operands.append(self.operands.pop() // self.operands.pop())
        elif op == 'DUP':
          self.operands.append(self.operands[-1])
        elif op == 'POP':
          self.operands.pop()
          if not self.operands:
            self.operands.append(0)
        elif op.isdigit():
          self.operands.append(int(op))
        else:
          self.operands = ['Invalid instruction: %s' % op]
​
  def getValue(self):
    return self.operands[-1]

