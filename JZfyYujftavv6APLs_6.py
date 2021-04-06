
import re
​
class Fraction:
​
  def __init__(self, a, b):
    if type(a) != int or type(b) != int or b == 0:
      print ('Initialisation Failed')
      exit()
    self.a = a
    self.b = b
  
  @staticmethod
  def __gcd(x, y):
    while y != 0:
      x, y = y, x % y
    return x
    
  def __str__(self):
    gcd = self.__gcd(self.a, self.b)
    return re.sub("^-", "- ",  "{}/{}".format(self.a // gcd, self.b//gcd))
  
  def __add__(self, other):
    d = self.b * other.b
    n = self.a * other.b + self.b * other.a
    gcd = self.__gcd(n, d)
    return Fraction(n // gcd, d // gcd)
    
  def __sub__(self, other):
    d = self.b * other.b
    n = self.a * other.b - self.b * other.a
    gcd = self.__gcd(n, d)
    return Fraction(n // gcd, d // gcd)
    
  def __mul__(self, other):  
    d = self.b * other.b
    n = self.a * other.a
    gcd = self.__gcd(n, d)
    return Fraction(n // gcd, d // gcd)
    
  def __truediv__(self, other):
    if other.b == 0:
      return "'Initialisation Failed'"
    d = self.b * other.a
    n = self.a * other.b
    gcd = self.__gcd(n, d)
    return Fraction(n // gcd, d // gcd)
    
  def __eq__(self, other):
    return self.a / self.b == other.a / other.b
    
  def __ne__(self, other):
    return self.a / self.b != other.a / other.b
    
  def __lt__(self, other):
    return (self.a /self.b) < (other.a / other.b)
    
  def __gt__(self, other):
    return (self.a /self.b) > (other.a / other.b)
    
  def __le__(self, other):
    return (self.a / self.b) <= (other.a - other.b)
    
  def __ge__(self, other):
    return (self.a / self.b) >= (other.a - other.b)
    
  def decimal(self):
    return round((self.a / self.b), 7)
    
  @classmethod
  def fraction(cls, decimal):
    gcd = cls_gcd(round(decimal) * 10000000, 10000000)
    return Fraction(int(decimal * gcd), int(gcd))

