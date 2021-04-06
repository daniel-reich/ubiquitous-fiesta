
class Number:
  def __init__(self, n): self.n = n
  __eq__ = lambda self, other: self.n == other
  __add__ = lambda self, other: self.n + other
  __radd__ = __add__
  __sub__ = lambda self, other: self.n - other
  __mul__ = lambda self, other: self.n * other
  __rmul__ = __mul__
  __truediv__ = lambda self, other: "ZeroDivisionError" if other == 0 else self.n / other
  __rtruediv__ = lambda self, other: "ZeroDivisionError" if self == 0 else other / self.n
  __int__ = lambda self: int(self.n)
  __float__ = lambda self: float(self.n)
  __str__ = lambda self: str(self.n)

