
class FourVector:
  value=[0.0,0.0,0.0,0.0]
  def __init__(self,a=[0.0,0.0,0.0,0.0]):
    self.value = a
  
  def GetComponents(self):
    return self.value
  
  def SetComponents(self,o):
    self.value=o
  
  def __eq__(self,o):
    return  max([abs(a-b) for a,b in zip(self.value,o.value)])==0
  
  def __add__(self,o):
    return  FourVector([a+b for a,b in zip(self.value,o.value)])
  def __sub__(self,o):
    return  FourVector([a-b for a,b in zip(self.value,o.value)])
  def __str__(self):
    out=[]
    for a in self.value: # how you would like to round 
      if type(a)==int:
        out.append(str(a))
      elif abs(a)>=1 or abs(a)==0.5:
        out.append('{:#.1f}'.format(a)) # 0.5
      else:
        out.append('{:#.2f}'.format(a)) #0.75
    
    return  "("+', '.join(out) + ")"

