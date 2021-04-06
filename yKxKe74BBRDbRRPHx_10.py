
class Number:
  def __init__(self, value):
    self._v = value
  def __repr__(self):
    return 'Number({})'.format(self._v)
  def __eq__(self, other):
    if type(other) == Number:
      return self._v == other._v
    return self._v == other
  def __int__(self):
    return int(self._v)
  def __float__(self):
    return float(self._v)
  def __str__(self):
    return str(self._v)
  def __add__(self, other):
    if type(other) == Number:
      return Number(self._v + other._v)
    return Number(self._v + other)
  def __sub__(self, other):
    return Number(self._v - other)
  def __rsub__(self, other):
    return Number(self._v - other)
  def __mul__(self, other):
    if type(other) == Number:
      return Number(self._v * other._v)
    return Number(self._v * other)
  def __rmul__(self, other):
    return Number(self._v * other)
  def __truediv__(self, other):
    try:
      if type(other) == Number:
        return Number(self._v / other._v)
      return Number(self._v / other)
    except ZeroDivisionError:
      return 'ZeroDivisionError'
  def __floordiv__(self, other):
    return Number(self._v // other._v)
  def __gt__(self, other):
    return self._v > other._v
  def __le__(self, other):
    return self._v <= other._v

