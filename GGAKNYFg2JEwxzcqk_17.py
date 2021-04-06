
def anti_divisors(n):
  def divisor(n1, n2):
    return n1%n2 == 0
  def is_even(n):
    return n%2==0
  
  ads = []
  for num in range(2, n):
    d = divisor(n, num)
    if d == False:
      even = is_even(num)
      if even == False:
        pd1 = n * 2 - 1
        pd2 = n * 2 + 1
        
        d1 = divisor(pd1, num)
        d2 = divisor(pd2, num)
        
        if d1 == True or d2 == True:
          ads.append(num)
      else:
        d1 = divisor(n*2, num)
        if d1 == True:
          ads.append(num)
    
  return ads

