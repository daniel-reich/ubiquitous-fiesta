
def simplify_frac(f):
  def GCD(n1, n2):
    def factors(n):
      facts = []
      for num in range(1, n + 1):
        if n%num == 0:
          facts.append(num)
      return facts
    
    n1factors = factors(n1)
    n2factors = factors(n2)
    
    common_denominators = []
  
    for factor in n1factors:
      if factor in n2factors:
        common_denominators.append(factor)
    
    return max(common_denominators)
  
  frac = f.split('/')
  
  numerator = int(frac[0])
  denominator = int(frac[1])
  
  gcd = GCD(numerator, denominator)
  
  numerator /= gcd
  denominator /= gcd
  
  return '{}/{}'.format(int(numerator), int(denominator))

