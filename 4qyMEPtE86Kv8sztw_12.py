
class Fraction:
  def dec_to_frac(decimal):
    
    a = int(decimal)
    b = 10 ** len(decimal)
​
    return Fraction(a,b)
  def GCF(n1, n2):
    def factor(num):
      return [n for n in range(1, num + 1) if num % n == 0]
    
    n1_fac = factor(n1)
    n2_fac = factor(n2)
​
    return max([fac for fac in n1_fac if fac in n2_fac])
​
  def __init__(self, a, b):
​
    self.gcd = Fraction.GCF(a, b)
​
    self.a = a // self.gcd
    self.b = b // self.gcd
​
  def __str__(self):
    return '{}/{}'.format(self.a, self.b)
  
  def __add__(self, other):
    return str(self) + other
  
  def __radd__(self, other):
    return other + str(self)
​
class Base:
​
  def __init__(self, base_val = 10):
    self.bv = base_val
  
  def convert_to_b10(self, value):
​
    whole_val, dec = value.split('.')
​
    if int(dec) > 0:
      dec_val = 0
      for n in range(len(dec)):
        if dec[n] == '1':
          dec_val += eval('1/{}'.format(self.bv ** (n + 1)))
    else:
      dec_val = 0
    
    place_vals = []
    expon = 0
​
    while len(place_vals) < len(whole_val):
      
      place_vals.append(self.bv ** expon)
      expon += 1
    
    place_vals = list(reversed(place_vals))
​
    whole_b10 = sum([int(whole_val[n]) * place_vals[n] for n in range(len(place_vals))])
​
    if '.' not in str(dec_val):
      fraction = ''
    else:
      fraction = ' ' + Fraction.dec_to_frac(str(dec_val).split('.')[1])
​
    return '{}'.format(whole_b10) + fraction
​
  def add(self, values = []):
    if len(values) <= 0:
      return False
    else:
      b10_vals = [self.convert_to_b10(value) for value in values]
      
      b10_dec_vals = [eval(str(value).replace(' ','+')) for value in b10_vals]
​
      try:
        whole, dec = str(sum(b10_dec_vals)).split('.')
      except ValueError:
        whole = str(sum(b10_dec_vals))
        dec = '0'
     # print(dec)
      if dec == '0':
        fraction = ''
      else:
        fraction = ' ' + Fraction.dec_to_frac(dec)
​
      if int(whole) > 0:
        return whole + fraction
      else:
        return str(fraction[1:])
​
​
def binary_sum(lst):
​
  b2 = Base(2)
​
  return b2.add(lst)   if b2.add(lst) != '' else '0'

