
class Number:
  def __init__(self, num):
    self.num = num
  def __int__(self):# Used in the "int" method
    return int(self.num)
  def __float__(self): # Used in the "float" method
    return float(self.num)
  def __str__(self): # Used in the "str" method
    return str(self.num) 
  def __repr__(self): # Used in the "repr" method
    return "Number({})".format(str(self.num))
  def __add__(self, other): # Used in the "+" operator function 
    return Number(self.num + (other.num if isinstance(other, Number) else other))
  __radd__ = __add__
  def __sub__(self, other): # Used in the "-" operator function 
    return Number(self.num - (other.num if isinstance(other, Number) else other))
  __rsub__ = __sub__
  def __mul__(self, other): # Used in the `*` operator function
    return Number(self.num * (other.num if isinstance(other, Number) else other))
  __rmul__ = __mul__
  def __truediv__(self, other): # Used in the "/" operator function
    try:
      return Number(self.num / (other.num if isinstance(other, Number) else other))
    except ZeroDivisionError:
      return "ZeroDivisionError"
  __rtruediv__ = __truediv__
  def __floordiv__(self, other): # Used in the "//" operator function
    try:
      return Number(self.num // (other.num if isinstance(other, Number) else other))
    except ZeroDivisionError:
      return "ZeroDivisionError"
  __rfloordiv__ = __floordiv__
  def __eq__(self, other): # ==
    return self.num == (other.num if isinstance(other, Number) else other)
  def __ne__(self, other): # !=
    return self.num != (other.num if isinstance(other, Number) else other)
  def __lt__(self, other): # <
    return self.num < (other.num if isinstance(other, Number) else other)
  def __le__(self, other): # <=
    return self.num <= (other.num if isinstance(other, Number) else other)
  def __gt__(self, other): # >
    return self.num > (other.num if isinstance(other, Number) else other)
  def __ge__(self, other): # >=
    return self.num >= (other.num if isinstance(other, Number) else other)
  def __bool__(self): # if Number(x):
    return True if self.num == 1 else False

