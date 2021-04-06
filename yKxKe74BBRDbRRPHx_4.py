
class Number:
  def __init__(self,num):
    self.value = num
  
  def __eq__(self, other):
    if isinstance(other, Number):
      return self.value == other.value
    return self.value == other
    
  def __ne__(self, other):
    if isinstance(other, Number):
      return self.value != other.value
    return self.value != other
    
  def __gt__(self, other):
    if isinstance(other, Number):
      return self.value > other.value
    return self.value > other
    
  def __le__(self, other):
    if isinstance(other, Number):
      return self.value <= other.value
    return self.value <= other
  
  def __int__(self):
    return int(self.value)
    
  def __float__(self):
    return float(self.value)
    
  def __str__(self):
    return str(self.value)
    
  def __repr__(self):
    return "Number(" + str(self.value) + ")"
    
  def __add__(self, other):
    if not isinstance(other, Number):
      other = Number(other)
    return Number(self.value + other.value)
  
  __radd__ = __add__
    
  def __sub__(self, other):
    if not isinstance(other, Number):
      other = Number(other)
    return Number(self.value - other.value)
    
  __rsub__ = __sub__
    
  def __mul__(self,other):
    if not isinstance(other, Number):
      other = Number(other)
    return Number(self.value * other.value)
    
  __rmul__ = __mul__
    
  def __truediv__(self, other):
    if not isinstance(other, Number):
      other = Number(other)
    if other.value == 0:
      return "ZeroDivisionError"
    return Number(self.value / other.value)
    
  __rtruediv__ = __truediv__
    
  def __floordiv__(self, other):
    if not isinstance(other, Number):
      other = Number(other)
    if other.value == 0:
      return "ZeroDivisionError"
    return Number(self.value // other.value)
    
  __rfloordiv__ = __floordiv__
  
  
​
obj2 = Number(5)

