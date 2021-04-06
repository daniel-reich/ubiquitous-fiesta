
class Number:
  
  def __init__(self, val):
    self.v = val
  
  def __add__(self, other):
    if isinstance(other, int) == True:
      return Number(self.v + other)
    else:
      return Number(self.v + other.v)
  
  def __sub__(self, other):
    if isinstance(other, int) == True:
      return Number(self.v - other)
    else:
      return Number(self.v - other.v)
  
  def __rsub__(self, other):
    return Number(other - self.v)
  
  def __mul__(self, other):
    if isinstance(other, int) == True:
      return Number(self.v * other)
    else:
      return Number(self.v * other.v)
  
  def __rmul__(self, other):
    print(self, other)
    return Number(self.v * other)
  
  def __truediv__(self, other):
    if other == 0 or other.v == 0:
      return 'ZeroDivisionError'
    if isinstance(other,int) == True:
      return Number(self.v / other)
    else:
      return Number(self.v/other.v)
  
  def __floordiv__(self, other):
    if other == 0 or other.v == 0:
      return 'ZeroDivisionError'
    if isinstance(other, int) == True:
      return Number(self.v//other)
    else:
      return Number(self.v//other.v)
  
  def __str__(self):
    return str(self.v)
  
  def __int__(self):
    return int(self.v)
  
  def __repr__(self):
    return 'Number({})'.format(self.v)
  
  def __float__(self):
    return float(self.v)
  
  def __eq__(self, other):
    print(self, other)
    if isinstance(other, int) == True:
      return self.v == other
    return self.v == other.v
  
  def __gt__(self, other):
    if isinstance(other, int) == True:
      return self.v > other
    return self.v > other.v
  
  def __ge__(self, other):
    if isinstance(other, int) == True:
      return self.v >= other
    return self.v >= other.v
  
  def __lt__(self, other):
    if isinstance(other, int) == True:
      return self.v < other
    return self.v < other.v
  
  def __le__(self, other):
    if isinstance(other, int) == True:
      return self.v <= other
    return self.v <= other.v

