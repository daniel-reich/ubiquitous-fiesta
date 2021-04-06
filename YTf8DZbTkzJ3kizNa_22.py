
def moran(n):
​
  def is_prime(num):
    for i in range(2, num):
      if num%i == 0:
        return False
    return True
    
  s = sum([int(x) for x in list(str(n))])
  if n%s == 0:
    if is_prime(n//s):
      return "M"
    else:
      return "H"
  else: 
    return "Neither"

