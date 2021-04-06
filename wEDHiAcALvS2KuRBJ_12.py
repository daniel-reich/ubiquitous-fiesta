
class StackCalc:
​
    def __init__(self):
      self.stack = []
    def run(self, instructions):
      if instructions == '':
        return
      if ' ' not in instructions:
        if instructions.isdigit():
          self.stack.append(int(instructions))
        else:
          self.stack.append(instructions)
      else:
        intsts = instructions.split(' ')
        for i in intsts:
          if i.isdigit():
            self.stack.append(int(i))
          elif i == '+' and len(self.stack)>=2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a+b)
          elif i == '-' and len(self.stack)>=2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a-b)
          elif i == '*' and len(self.stack)>=2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a*b)
          elif i == '/' and len(self.stack)>=2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a/b)
          elif i == 'DUP' and len(self.stack)>=1:
            self.stack.append(self.stack[-1])
          elif i == 'POP' and len(self.stack)>=1:
            self.stack = self.stack[:-1]
          else:
            self.stack.append(i)
            return
    def getValue(self):
      if len(self.stack)>=1:
        if type(self.stack[-1]) == type('a'):
          return 'Invalid instruction: ' + self.stack[-1]
        a = self.stack.pop()
        return a
      else:
        return 0

