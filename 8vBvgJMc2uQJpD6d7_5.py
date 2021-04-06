
def get_prime_factor(num):
  for x in range(2, num+1):
    if num % x == 0:
      return x
​
def prime_factors(num):
  res = []
  
  while 1:
    x = get_prime_factor(num)
    if not x:
      break
    res.append(x)
    num = num // x
    
  return res

