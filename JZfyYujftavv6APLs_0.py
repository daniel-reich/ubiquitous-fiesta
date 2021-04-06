
class Fraction:
  def __init__ (self,a,b):
    self.valid = type(a)==type(b)==int and b!=0
    if self.valid:
      if b<0:
        a,b = -a,-b
      d = gcd(abs(a),b)
      self.num = a//d
      self.den = b//d
  
  @classmethod
  def fraction(cls, flo):
    s = str(flo)
    idx = s.index('.')
    return Fraction(int(s.replace('.','')), 10**(len(s)-1-idx))
  
  def __eq__ (self, other):
    return self.num == other.num and self.den == other.den
  
  def __add__(self, other):
    return Fraction(self.num*other.den + self.den*other.num, self.den*other.den)
​
  def __sub__(self, other):
    return Fraction(self.num*other.den - self.den*other.num, self.den*other.den)
​
  def __mul__(self, other):
    return Fraction(self.num*other.num, self.den*other.den)
​
  def __truediv__(self, other):
    if other.num:
      return Fraction(self.num*other.den, self.den*other.num)
​
  def __gt__ (self, other):
    return self.num*other.den > self.den*other.num
​
  def __ge__ (self, other):
    return self.num*other.den >= self.den*other.num
    
  def __str__ (self):
    if self.valid:
      return '{}{}/{}'.format('' if self.num>=0 else '- ',abs(self.num),self.den)
    return 'Initialisation Failed'
    
  def __repr__(self):
    return str(self)
    
  def decimal(self):
    return round(self.num/self.den,7)
​
​
​
def gcd(a,b):
  while a>0:
    a,b = b%a,a
  return b

