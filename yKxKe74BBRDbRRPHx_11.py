
class Number():
  def __init__(self,n):
    self.n = n
  def __eq__(self,a):
    a = a.n if isinstance(a , Number) else a
    return self.n==a
  def __lt__(self,a):
    a = a.n if isinstance(a , Number) else a
    return self.n<a
  def __le__(self,a):
    a = a.n if isinstance(a , Number) else a
    return self.n<=a
  def __gt__(self,a):
    a = a.n if isinstance(a , Number) else a
    return self.n>a
  def __ge__(self,a):
    a = a.n if isinstance(a , Number) else a
    return self.n>=a
​
  def __int__(self):
    return int(self.n)
  def __float__(self):
    return float(self.n)
  def __str__(self):
    return str(self.n)
  def __repr__(self):
    return 'Number({})'.format(self.n)
  def __add__(self,a):
    return self.n+a.n if isinstance(a , Number) else self.n+a
  def __sub__(self,a):
    return self.n-a.n if isinstance(a , Number) else self.n-a
  def __rsub__(self,a):
    return a.n-self.n if isinstance(a , Number) else a-self.n
  def __mul__(self,a):
    return self.n*a.n if isinstance(a , Number) else self.n*a
  def __rmul__(self,a):
    return self.n*a.n if isinstance(a , Number) else self.n*a
  def __truediv__(self,a):
    return (self.n/a.n if a.n else 'ZeroDivisionError') if isinstance(a , Number) else (self.n/a if a else 'ZeroDivisionError')
  def __rtruediv__(self,a):
    return (a.n/self.n if self.n else 'ZeroDivisionError') if isinstance(a , Number) else (a/self.n if self.n else 'ZeroDivisionError')
  def __floordiv__(self,a):
    return self.n//a.n if isinstance(a , Number) else self.n//a

