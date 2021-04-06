
class FourVector:
​
  def __init__(self, points = [0,0,0,0]):
    self.points = points
  
    self.A = points[0]
    self.B = points[1]
    self.C = points[2]
    self.D = points[3]
  
  def __add__(self, other):
​
    return FourVector([(self.A + other.A), (self.B + other.B), (self.C + other.C), (self.D + other.D)])
  
  def __sub__(self, other):
    return FourVector([(self.A - other.A), self.B - other.B, self.C - other.C, self.D - other.D])
​
  def GetComponents(self):
    return self.points
​
  def SetComponents(self, components):
    self.points = components
​
    self.A = components[0]
    self.B = components[1]
    self.C = components[2]
    self.D = components[3] 
​
    return True
  
  def __str__(self):
    return '({}, {}, {}, {})'.format(round(self.A,3), round(self.B,3), round(self.C,3), round(self.D, 3))
​
  def __eq__(self, other):
    return  v0a

