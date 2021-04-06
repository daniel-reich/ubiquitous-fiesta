
class Number:
  def __init__(self,num):
    self.num = num
    
  def __add__(self,other):
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a+b)
    
  def __sub__(self,other):
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a-b)
    
  def __rsub__(self,other):
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a-b)
    
  def __mul__(self,other):
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a*b)
    
  def __rmul__(self,other):
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a*b)
  
  def __truediv__(self,other):
    if other==0 or type(other)!=int and other.num==0:
      return 'ZeroDivisionError'
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a/b)
    
  def __floordiv__(self,other):
    if other==0 or type(other)!=int and other.num==0:
      return 'ZeroDivisionError'
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return Number(a//b)
    
  def __eq__(self,other):
    a = self.num if type(self)==Number else self
    b = other.num if type(other)==Number else other
    return a==b
  
  def __gt__(self,other):
    return self.num>other.num
  
  def __le__(self,other):
    return self.num<=other.num
    
  def __repr__(self):
    return "Number({})".format(self.num)
    
  def __str__(self):
    return str(self.num)
  
  def __int__(self):
    return int(self.num)
    
  def __float__(self):
    return float(self.num)

