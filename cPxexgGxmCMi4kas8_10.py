
class FourVector:
  def __init__(self, components=None):
    if components is None:
      components = [0.0, 0.0, 0.0, 0.0]
    self.SetComponents(components)
  
  def GetComponents(self):
    return [self.a, self.b, self.c, self.d]
  
  def SetComponents(self, components):
    a, b, c, d = components
    self.a = a
    self.b = b
    self.c = c
    self.d = d
  
  def __add__(self, other):
    return FourVector([
      self.a + other.a,
      self.b + other.b,
      self.c + other.c,
      self.d + other.d
    ])
  
  def __sub__(self, other):
    return FourVector([
      self.a - other.a,
      self.b - other.b,
      self.c - other.c,
      self.d - other.d
    ])
  
  def __eq__(self, other):
    return all([
      self.a == other.a,
      self.b == other.b,
      self.c == other.c,
      self.d == other.d,
    ])
  
  def __str__(self):
    return '({}, {}, {}, {})'.format(
      round(self.a, 3), round(self.b, 3),
      round(self.c, 3), round(self.d, 3)
    )

