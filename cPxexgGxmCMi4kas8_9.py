
class FourVector:
  def __init__(self, vectors = [0,0,0,0]):
    self.vectors = vectors
  
  def __eq__ (self, other):
    return self.vectors == other.vectors
    
  def GetComponents(self):
    return self.vectors
  
  def SetComponents(self, vectors):
    self.vectors = vectors
    
  def __add__(self, other):
    return FourVector([sum(z) for z in zip(self.vectors, other.vectors)])
  
  def __sub__(self, other):
    return FourVector([z[0]-z[1] for z in zip(self.vectors, other.vectors)])
  
  def __str__(self):
    return "({}, {}, {}, {})".format(*[round(v,3) for v in self.vectors])

