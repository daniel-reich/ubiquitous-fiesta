
import operator
​
class StackCalc:
  genOperators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
  }
  
  def __init__(self):
    self.stack = []
​
  def run(self, instructions):
    values = instructions.split(" ")
    for val in values:
      if val.isdigit():
        self.stack.append(int(val))
      elif val in self.genOperators.keys() and len(self.stack) >= 2:
        self.stack[-2] = self.genOperators[val](self.stack[-1], self.stack[-2])
        self.stack.pop()
      elif val == "DUP":
        self.stack.append(self.stack[-1])
      elif val == "POP":
        self.stack.pop()
      elif val == "":
        self.stack = [0]
        break
      else:
        self.stack = ["Invalid instruction: {}".format(val)]
        break
    if self.stack == []:
      self.stack = [0]
    return self.stack[-1]
      
  def getValue(self):
    return self.stack[-1]

