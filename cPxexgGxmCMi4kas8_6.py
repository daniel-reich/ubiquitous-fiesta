
class FourVector():
  def __init__(self,v=None): self.v= [0.0, 0.0, 0.0, 0.0] if v is None else v
  def GetComponents(self): return self.v
  def SetComponents(self,v): self.v=v
  def __add__(self,other): return FourVector(list(a+b for a,b in zip(self.v,other.v)))
  def __sub__(self,other): return FourVector(list(a-b for a,b in zip(self.v,other.v)))
  def __eq__(self,other): return self.v==other.v
  def __str__(self): return str(tuple(round(e,3) for e in self.v))

