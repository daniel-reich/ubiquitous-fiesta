
def decorator(func):
    def wrapper(*args):
        if isinstance(args[1], Number):
            return func(*args)
        else:
            return func(args[0], Number(args[1]))
    return wrapper
​
class Number:
  def __init__(self, value):
    self.value = value
  
  @decorator
  def __eq__(self, other):
    return self.value == other.value
  
  @decorator
  def __add__(self, other):
    return Number(self.value + other.value)
    
  @decorator  
  def __sub__(self, other):
    return Number(self.value - other.value)
  
  @decorator
  def __mul__(self, other):
    return Number(self.value * other.value)
  
  @decorator
  def __truediv__(self, other):
    if other.value == 0:
      return 'ZeroDivisionError'
    else:
      return Number(self.value / other.value)
  
  def __str__(self):
    return str(self.value)
    
  def __int__(self):
    return int(self.value)
    
  def __float__(self):
    return float(self.value)

