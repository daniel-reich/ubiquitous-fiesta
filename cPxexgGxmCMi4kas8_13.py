
class FourVector:
  def __init__(self,vector = [0.0,0.0,0.0,0.0]):
    self.vector = vector
  def SetComponents(self,v):
    self.vector = v
  def GetComponents(self):
    return self.vector
  def __add__(self,v2):
    return FourVector(list(map(lambda x:x[0] + x[1],zip(self.vector,v2.vector))))
  def __sub__(self,v2):
    return FourVector(list(map(lambda x:x[0] - x[1],zip(self.vector,v2.vector))))
  def __eq__(self,v2):
    return self.vector == v2.vector
  def __str__(self):
    return '(' + ', '.join(list(map(lambda x: str(round(x,3)),self.vector))) + ')'

