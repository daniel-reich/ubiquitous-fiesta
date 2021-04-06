
class StackCalc:
​
  def __init__(self):
    self.stack = []
  def run(self, instructions):
    inst = instructions.split()
    for ins in inst:
      if ins.isdigit():
        self.stack.append(int(ins))
      elif ins == "+":
        pop1, pop2 = (self.stack.pop(), self.stack.pop())
        self.stack.append(pop1 + pop2)
      elif ins == "-":
        pop1, pop2 = (self.stack.pop(), self.stack.pop())
        self.stack.append(pop1 - pop2)
      elif ins == "*":
        pop1, pop2 = (self.stack.pop(), self.stack.pop())
        self.stack.append(pop1 * pop2)
      elif ins == "/":
        pop1, pop2 = (self.stack.pop(), self.stack.pop())
        self.stack.append(pop1 / pop2)
      elif ins == "DUP":
        self.stack.append(self.stack[-1])
      elif ins == "POP":
        self.stack.pop()
      else:
        self.stack.append("Invalid instruction: {}".format(ins))
        break
      
  def getValue(self):
    return 0 if len(self.stack) == 0 else self.stack[-1]

