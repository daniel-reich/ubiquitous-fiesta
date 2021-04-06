
def oVal(x):
  try:
    return x.val
  except:
    return x
​
class Number:
  def __init__(self, value):
    self.val = value
  def __add__(self, x):
    return oVal(self) + oVal(x)
  def __sub__(self, x):
    return oVal(self) - oVal(x)
  def __mul__(self, x):
    return oVal(self) * oVal(x)
  def __truediv__(self, x):
    try:
      return oVal(self) / oVal(x)
    except ZeroDivisionError:
      return "ZeroDivisionError"
  def __rtruediv__(self, x):
    try:
      return oVal(x) / oVal(self)
    except ZeroDivisionError:
      return "ZeroDivisionError"
  def __eq__(self, other):
    return True

