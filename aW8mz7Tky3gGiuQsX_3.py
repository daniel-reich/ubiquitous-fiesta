
def is_powerful(n):
  def Prime_Factors(n):
    factors = []
    
    for num in range(2, n):
      while n%num == 0:
        factors.append(num)
        n /= num
    return list(set(factors))
  def Factors(n):
    facts = []
    
    for num in range(2, n):
      if n%num == 0:
        facts.append(num)
    
    return facts
  
  pf = Prime_Factors(n)
  fs = Factors(n)
  
  squares = []
  
  for prime in pf:
    squares.append(prime**2)
  
  for square in squares:
    if square not in fs:
      return False
  return True

