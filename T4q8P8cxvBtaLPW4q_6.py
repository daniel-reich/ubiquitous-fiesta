
def is_prime(n):
  if n == 2 or n == 3:
    return True
  if n < 2 or n%2 == 0:
    return False
  if n < 9:
    return True
  if n%3 == 0:
    return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0:
      return False
    if n % (f+2) == 0:
      return False
    f += 6
  return True 
    
​
 
def extract_primes(num):
  r = list(str(num))
  res = []
  for n in range(1, len(r)+1):
    for i, digit in enumerate(r):
      if i+n <= len(r) and r[i] != '0':
        res.append(
        int(''.join(r[i: i+n]))
        )
        
  return sorted(filter(is_prime, res))

