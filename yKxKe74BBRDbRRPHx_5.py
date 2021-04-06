
class Number:
  def __init__(self, n):
    self.n = n
  def __eq__(self, o):
    if isinstance(o, Number):
      return self.n == o.n
    return self.n == o
  def __ne__(self, o):
    if isinstance(o, Number):
      return self.n != o.n
    return self.n != o
  def __lt__(self, o):
    if isinstance(o, Number):
      return self.n < o.n
    return self.n < o
  def __le__(self, o):
    if isinstance(o, Number):
      return self.n <= o.n
    return self.n <= o
  def __gt__(self, o):
    if isinstance(o, Number):
      return self.n > o.n
    return self.n > o
  def __ge__(self, o):
    if isinstance(o, Number):
      return self.n >= o.n
    return self.n >= o
  def __int__(self):
    return int(self.n)
  def __float__(self):
    return float(self.n)
  def __str__(self):
    return str(self.n)
  __repr = __str__
  def __add__(self, o):
    if isinstance(o, Number):
      return Number(self.n + o.n)
    return Number(self.n + o)
  __radd__ = __add__
  def __sub__(self, o):
    if isinstance(o, Number):
      return Number(self.n - o.n)
    return Number(self.n - o)
  __rsub__ = __sub__
  def __mul__(self, o):
    if isinstance(o, Number):
      return Number(self.n * o.n)
    return Number(self.n * o)
  __rmul__ = __mul__
  def __truediv__(self, o):
    if o == 0:
      return 'ZeroDivisionError'
    if isinstance(o, Number):
      return Number(self.n / o.n)
    return Number(self.n / o)
  def __floordiv__(self, o):
    if o == 0:
      return 'ZeroDivisionError'
    if isinstance(o, Number):
      return Number(self.n // o.n)
    return Number(self.n // o)
    
obj2 = Number(5) #Fix test case bug

