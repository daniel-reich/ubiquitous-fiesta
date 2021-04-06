
class StackCalc:
​
  def __init__(self):
    pass
​
  def run(self, instructions):
    s = [0]
    for x in instructions.split():
      if x.isdigit():
        s.append(int(x))
      elif x == '+':
        s.append(s.pop() + s.pop())
      elif x == '-':
        s.append(s.pop() - s.pop())
      elif x == '*':
        s.append(s.pop() * s.pop())
      elif x == '/':
        s.append(s.pop() / s.pop())
      elif x == 'DUP':
        x = s.pop()
        s.append(x)
        s.append(x)
      elif x == 'POP':
        s.pop()
      else:
        self.value = 'Invalid instruction: ' + x
        return
    self.value = s.pop()
​
  def getValue(self):
    return self.value

