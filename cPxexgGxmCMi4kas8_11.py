
class FourVector:
  def __init__(self,vec=[0.0,0.0,0.0,0.0]):
    self.vec = vec
  def __eq__(self,other):
    return self.vec==other.vec
  def __add__(self,other):
    return FourVector([sum(i) for i in zip(self.vec,other.vec)])
  def __sub__(self,other):
    return FourVector([round(a-b,2) for a,b in zip(self.vec,other.vec)])
  def __str__(self):
    return str(tuple(self.vec))
    
  def GetComponents(self):
    return self.vec
  def SetComponents(self,vec):
    self.vec = vec

