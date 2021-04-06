
class Number:
  
  def __init__(self, n):
    self.n = n
    
  def __str__(self):
    return str(self.n)
  
  def __int__(self):
    return int(self.n)
    
  def __float__(self):
    return float(self.n)
    
  def __eq__(self, other):
    if isinstance(other, Number):
      return self.n == other.n
    else:
      return self.n == other
  
  def __gt__(self, other):
    return self.n > other.n
    
  def __le__(self, other):
    return self.n <= other.n
    
  def __add__(self, other):
    if isinstance(other, Number):
      y = self.n + other.n
    else:
      y = self.n + other
    return Number(y)
  
  def __sub__(self, other):
    if isinstance(other, Number):
      y = self.n - other.n
    else:
      y = self.n - other
    return Number(y)
  
  def __rsub__(self, other):
    if isinstance(other, Number):
      y = self.n - other.n
    else:
      y = self.n - other
    return Number(y)
  
  def __mul__(self, other):
    if isinstance(other, Number):
      y = self.n * other.n
    else:
      y = self.n * other
    return Number(y)
    
  def __rmul__(self, other):
    if isinstance(other, Number):
      y = self.n * other.n
    else:
      y = self.n * other
    return Number(y)
  
  def __truediv__(self, other):
    try:
      if isinstance(other, Number):
        y = self.n / other.n
      else:
        y = self.n / other
      return Number(y)
    except ZeroDivisionError:
      return 'ZeroDivisionError'
  
  def __floordiv__(self, other):
    try:
      if isinstance(other, Number):
        y = self.n // other.n
      else:
        y = self.n // other
      return Number(y)
    except ZeroDivisionError:
      return 'ZeroDivisionError'
  
obj2 = Number(5)

