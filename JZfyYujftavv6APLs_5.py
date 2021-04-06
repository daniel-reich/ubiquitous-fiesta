
from fractions import gcd
​
class Fraction:
  def __init__(self, numerator, denominator):
    if not isinstance(numerator, int) or not isinstance(denominator, int) or denominator == 0:
      print("Initialisation Failed")
    else:
      g = gcd(numerator, denominator)
      self.numerator = numerator // g
      self.denominator = denominator // g
  
  def is_valid(self):
    return hasattr(self, 'numerator') and hasattr(self, 'denominator')
​
  def __str__(self):
    if not self.is_valid():
      return "Initialisation Failed"
    sign = -1 if self.numerator * self.denominator < 0 else 1
    return '{}{}/{}'.format('- ' if sign<0 else '', abs(self.numerator), abs(self.denominator))
​
  def __add__(a, b):
    if not a.is_valid() or not b.is_valid():
      return "Initialisation Failed"
    return Fraction(a.numerator + b.numerator, a.denominator + b.denominator)
​
  def __add__(a, b):
    if not a.is_valid() or not b.is_valid():
      return "Initialisation Failed"
    return Fraction(a.numerator * b.denominator + b.numerator * a.denominator, a.denominator * b.denominator)
​
  def __sub__(a, b):
    if not a.is_valid() or not b.is_valid():
      return "Initialisation Failed"
    return Fraction(a.numerator * b.denominator - b.numerator * a.denominator, a.denominator * b.denominator)
​
  def __mul__(a, b):
    if not a.is_valid() or not b.is_valid():
      return "Initialisation Failed"
    return Fraction(a.numerator * b.numerator, a.denominator * b.denominator)
​
  def __truediv__(a, b):
    if not a.is_valid() or not b.is_valid():
      return "Initialisation Failed"
    return Fraction(a.numerator * b.denominator, a.denominator * b.numerator)
​
  def __eq__(a, b):
    if not a.is_valid() or not b.is_valid():
      return "Initialisation Failed"
    return a.numerator * b.denominator == a.denominator * b.numerator
​
  def __ne__(a, b):
    if not a.is_valid() or not b.is_valid():
      return "Initialisation Failed"
    return a.numerator * b.denominator != a.denominator * b.numerator
​
  def __lt__(a, b):
    if not a.is_valid() or not b.is_valid():
      return "Initialisation Failed"
    return a.numerator * b.denominator < a.denominator * b.numerator
​
  def __le__(a, b):
    if not a.is_valid() or not b.is_valid():
      return "Initialisation Failed"
    return a.numerator * b.denominator <= a.denominator * b.numerator
​
  def __gt__(a, b):
    if not a.is_valid() or not b.is_valid():
      return "Initialisation Failed"
    return a.numerator * b.denominator > a.denominator * b.numerator
​
  def __ge__(a, b):
    if not a.is_valid() or not b.is_valid():
      return "Initialisation Failed"
    return a.numerator * b.denominator >= a.denominator * b.numerator
​
  def decimal(self):
    if not self.is_valid() or not self.is_valid():
      return "Initialisation Failed"
    return round(self.numerator/self.denominator, 7)
​
  def fraction(dec):
    s = str(dec)
    return Fraction(int(s.replace('.', '')), 10**(len(s) - s.index('.') - 1))

