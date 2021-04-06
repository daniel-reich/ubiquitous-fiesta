
class FourVector:
  def __init__(self, v=[0,0,0,0]):
    self.vec = v
  
  def GetComponents(self):
    return self.vec
    
  def SetComponents(self, v):
    self.vec = v
  
  def __eq__(self, other):
    return self.vec == other.vec
  
  def __add__(self, other):
    return FourVector([self.vec[i]+other.vec[i] for i in range(4)])
​
  def __sub__(self, other):
    return FourVector([self.vec[i]-other.vec[i] for i in range(4)])
  
  def __str__(self):
    return str(tuple([round(c,3) for c in self.vec]))

