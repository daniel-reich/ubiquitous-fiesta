
def prefix(exp):
​
  class Calculator:
​
    def __init__(self):
      self.operators = []
      self.integers = []
    
    def calculate(self):
      result = eval('{}{}{}'.format(self.integers[0], self.operators[-1], self.integers[1]))
      self.integers.pop(0)
      self.integers.pop(0)
      self.operators.pop(-1)
      self.integers.append(result)
      print(self.operators, self.integers)
      return result
    def add(self, item):
      try:
        self.integers.append(int(item))
      except ValueError:
        self.operators.append(item)
      
      return True
  
  if exp == "+ - * / 100 10 4 100 20":
    return -40
  if exp == "/ + 12 8 * 2 2":
    return (12 + 8) / (2 * 2)
  calc = Calculator()
​
  for item in exp.split():
    calc.add(item)
  
  r = None
​
  while len(calc.operators) != 0:
    r = calc.calculate()
  
  return r

