
from math import factorial
def Formula(n):
  def term(char,number):
    return "" if number == 0 else char if number == 1 else char + "^" + str(number)
  class Binomial:
    def __init__(self,k):
      self.c = factorial(abs(n)) // (factorial(abs(n)-k) * factorial(k))
      self.k = k
    def coefficient(self):
      return "" if self.c <= 1 else str(self.c)
    def string(self):
      return str(self.coefficient()) + term("a",abs(n)-self.k) + term("b",self.k)
    def plus(self):
      return "" if self.c == 0 or self.k == abs(n) else "+"
  terms = [Binomial(i) for i in range(0,abs(n)+1)]
  s = ''.join(list(map(lambda x: x.string() + x.plus(),terms)))
  return "1" if n == 0 else s if n > 0 else "1/({})".format(s)

