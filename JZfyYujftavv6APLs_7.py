
def gcd(x, y): 
  while(y): 
    x, y = y, x % y 
  return x 
  
class Fraction:
  def __init__(self,a,b):
    if isinstance(a,int) and isinstance(b,int) and b!= 0:
      self.a = a//gcd(abs(a),abs(b))*b//abs(b)
      self.b = abs(b)//gcd(abs(a),abs(b))
      self.init = True
    else:
      self.msg = "Initialisation Failed"
      self.init = False
​
  def __str__ (self):
    if self.init:
      if self.a < 0:
        return "- {:d}/{:d}".format(abs(self.a),abs(self.b))
      else:
        return "{:d}/{:d}".format(abs(self.a),abs(self.b))
    else:
      return self.msg
  
  def __eq__(self, other):
    if isinstance(self, Fraction):
      if isinstance(other, Fraction): 
        return abs(self.a / self.b - other.a / other.b) < 10**-7
      else:
        return abs(self.a / self.b - other) < 10**-7
    else:
      if isinstance(other, Fraction):
        return abs(self - other.a / other.b) < 10**-7
      else:
        return abs(self - other) < 10**-7
​
  def __ne__(self, other):
    return not self.__eq__(other)
​
  def __gt__(self, other):
    return self.a / self.b > other.a / other.b
  
  def __ge__(self, other):
    return self.a / self.b >= other.a / other.b
  
  def __lt__(self, other):
    return self.a / self.b < other.a / other.b
  
  def __le__(self, other):
    return self.a / self.b <= other.a / other.b
    
  
  def __add__(self,other):
    return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)
​
  def __sub__(self,other):
    return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)
​
  def __mul__(self,other):
    return Fraction(self.a * other.a, self.b * other.b)
​
  def __truediv__(self,other):
    if other.a == 0:
      return None
    else:
      return Fraction(self.a * other.b, self.b * other.a)
​
  def decimal(self):
    return round(self.a/self.b,7)
​
  def fraction(x):
    return Fraction(int(x*10**7), 10**7)

