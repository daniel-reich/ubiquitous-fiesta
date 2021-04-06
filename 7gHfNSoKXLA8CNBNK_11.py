
def sim_prop_frac(max_den):
​
  class Fraction:
​
    def __init__(self, numerator, denominator):
      self.n = numerator
      self.d = denominator
    
    def simplify(self):
      def GCD(n1, n2):
​
        n1factors = []
        n2factors = []
​
        for n in range(1, min([n1, n2]) + 1):
​
          if n1 % n == 0:
            n1factors.append(n)
          if n2 % n == 0:
            n2factors.append(n)
        
        for factor in reversed(n1factors):
          if factor in n2factors:
            return factor
      
      gcd = GCD(self.n, self.d)
    
      self.n /= gcd
      self.d /= gcd
​
      return '{}/{}'.format(self.n, self.d)
  
  fractions = []
​
  for n in range(2, max_den + 1):
    for num in range(1, n):
      frac = Fraction(num, n)
      fractions.append(frac)
  
  simplified = set()
​
  for frac in fractions:
    simplified.add(frac.simplify())
  
  return len(list(simplified))

