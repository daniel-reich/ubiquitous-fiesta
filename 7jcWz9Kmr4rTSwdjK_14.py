
def prime_factorize(num):
  n = num
  factors = []
  i = 2
  
  while n > 1:
    if n % i == 0:
      n //= i
      factors.append(i)
    else:
      i += 1
      
  return factors

