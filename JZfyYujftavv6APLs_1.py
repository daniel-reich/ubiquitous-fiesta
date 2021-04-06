
class Fraction:
  def __init__(self,a=0,b=1):
    if type(a)==int and type(b)==int and b!=0:
      x,y=a,b
      while y:x,y=y,x%y
      self.a=abs(a)//x*(1,-1)[Fraction.sign(a*b)=='-']
      self.b=abs(b)//x
  def __str__(self):
    try:return('- %s/%s'if Fraction.sign(self.a*self.b)else'%s/%s')%(abs(self.a),abs(self.b))
    except:return'Initialisation Failed'
  def __add__(self,f):
    x,y=self.b,f.b
    while y:x,y=y,x%y
    l=self.b*f.b//x
    return Fraction(l//self.b*self.a+l//f.b*f.a,l)
  def __truediv__(self,f):
    if f.a:return self*Fraction(f.b,f.a)
  __sub__=lambda self,f:self.__add__(-f)
  __neg__=lambda self:Fraction(-self.a,self.b)
  __mul__=lambda self,f:Fraction(self.a*f.a,self.b*f.b)
  __eq__=lambda self,f:self.a*f.b-self.b*f.a<10**-7
  __lt__=lambda self,f:self.a*f.b<self.b*f.a
  __gt__=lambda self,f:self.a*f.b>self.b*f.a
  __le__=lambda self,f:self.a*f.b<=self.b*f.a
  __ge__=lambda self,f:self.a*f.b>=self.b*f.a
  decimal=lambda self:round(self.a/self.b,7)
  @staticmethod 
  def sign(v):return('','-')[v<0]
  @classmethod
  def fraction(cls,v):
    v=str(round(v,7))
    return Fraction(int(v.replace('.','')),10**(len(v)-1))

