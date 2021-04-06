
class FourVector:
  def __init__(self,v=None):
    if v is None:self.v=[0,0,0,0]
    else:self.v=v
  GetComponents=lambda self:self.v
  def SetComponents(self,v):
    self.v=v
  __add__=lambda self,f:FourVector([x+y for x,y in zip(self.v,f.v)])
  __sub__=lambda self,f:FourVector([x-y for x,y in zip(self.v,f.v)])
  __eq__=lambda self,f:all(x==y for x,y in zip(self.v,f.v))
  __str__=lambda self:str(tuple(round(x,3)for x in self.v))
  __repr__=lambda self:str(tuple(round(x,3)for x in self.v))

