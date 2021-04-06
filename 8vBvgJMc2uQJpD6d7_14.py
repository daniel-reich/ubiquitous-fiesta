
def prime_factors(n):
  r = []
  i = 2
  
  while n > 1:
    if n%i == 0:
      r.append(i)
      n /= i
    else:
      i += 1
    
  return r

