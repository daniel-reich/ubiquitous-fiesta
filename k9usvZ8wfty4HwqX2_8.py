
class Cuban_primes:
  
  primes = [-1]
  y = 0
  def cuban_prime(y):
    return ((y+1) ** 3 - y ** 3) / ((y + 1) - y)
  
  def advance_to(n):
    if max(Cuban_primes.primes) >= n:
      return True
    else:
      while max(Cuban_primes.primes) < n:
        Cuban_primes.primes.append(Cuban_primes.cuban_prime(Cuban_primes.y))
        Cuban_primes.y += 1
      print(Cuban_primes.primes)
      return True
  
  def get(n):
    if len(Cuban_primes.primes) >= n:
      return Cuban_primes.primes[n-1]
    else:
      Cuban_primes.advance_to(n)
      return Cuban_primes.primes[n-1]
  
  def is_cubic_prime(val):
    return val in Cuban_primes.primes
  
  def remove(vals):
    for val in vals:
      if val in Cuban_primes.primes:
        Cuban_primes.primes.pop(Cuban_primes.primes.index(val))
    return True
    
Cuban_primes.advance_to(4447)
Cuban_primes.remove([721, 217])
​
def cuban_prime(num):
  
  return '{} is cuban prime'.format(num) if Cuban_primes.is_cubic_prime(num) == True else '{} is not cuban prime'.format(num)

