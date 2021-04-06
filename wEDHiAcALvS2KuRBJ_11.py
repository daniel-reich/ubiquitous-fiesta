
class StackCalc:
​
  def __init__(self):
    self.result = []
  def run(self, instructions): 
    operators = '+-*/DUPPOPPSH'
    if instructions == '':
      self.result.append(0)
    else:
      for i in instructions.split(' '):
        if i.isdigit():
          self.result.append(int(i))
        elif i in operators:
          if i == '+':
            a = self.result.pop() + self.result.pop()
            self.result.append(a)
          elif i == '-':
            a = self.result.pop()
            b = self.result.pop()
            self.result.append(max(a,b)-min(a,b))
          elif i == '*':
            a = self.result.pop() * self.result.pop()
            self.result.append(a)
          elif i == '/':
            a = self.result.pop()
            b = self.result.pop()
            self.result.append(max(a,b)/min(a,b))
          elif i == 'DUP':
            self.result.append(self.result[-1])
          elif i == 'POP':
            del self.result[-1]
        elif i.isalpha():
          self.result.append('Invalid instruction: {}'.format(i))
          break
          
  def getValue(self):
    if self.result == []:
      return 0
    else:
      return self.result[-1]

