
class StackCalc:
  
  def __init__(self, value=0):
    self.value = 0
  
  def run(self, instructions):
    stack = []
    for item in instructions.split():
      if item.isnumeric():
        stack += [int(item)]
      elif item == "+":
        stack = stack[:-2] +[sum(stack[-2:])]
      elif item == "-":
        stack = stack[:-2] + [max(stack[-2:]) - min(stack[-2:])]
      elif item == "*":
        stack = stack[:-2] + [stack[-2:][0] * stack[-2:][1]]
      elif item == "/":
        stack = stack[:-2] + [max(stack[-2:]) / min(stack[-2:])]
      elif item == "DUP":
        stack += stack[-1:]
      elif item == "POP":
        if stack != []:
          stack = stack[:-1]
      else:
        stack = ["Invalid instruction: " + item]
        break
    if stack != []:
      self.value = stack[-1]
    
  
  def getValue(self):
      return self.value

