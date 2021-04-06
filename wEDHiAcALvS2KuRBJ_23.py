
class StackCalc:
​
  def __init__(self):
    self.stack = []
    self.inp_parsed = []
    self.invalid = False
  def run(self, instructions):
    inp_parsed = instructions.split(" ")
    for el in inp_parsed:
      if el.isnumeric():
        self.stack.append(int(el))
      elif el in ["+", "-", "*", "/"]:
        num1 = self.stack.pop()
        num2 = self.stack.pop()
        if el == "+":
          self.stack.append(num1 + num2)
        elif el == "-":
          self.stack.append(num1 - num2)
        elif el == "*":
          self.stack.append(num1 * num2)
        else:
          self.stack.append(num1 / num2)
      elif el == "DUP":
        self.stack.append(self.stack[-1])
      elif el == "POP":
        if self.stack:
          self.stack.pop()
      elif el.isalpha():
        self.stack = [el]
        self.invalid = True
        break
        
  def getValue(self):
    if self.stack:
      if self.invalid:
        return "Invalid instruction: {}".format(self.stack[0])
      return self.stack.pop()
    return 0

