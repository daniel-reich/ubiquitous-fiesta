
import math
def bemirp(n):
  if not isprime(n): return 'C'
  
  reverse = int(str(n)[::-1])
  if reverse == n or not isprime(reverse): return 'P'
  if any(ch not in '01689' for ch in str(n)): return 'E'
​
  flipped = int(str(n).replace('6','a').replace('9','6').replace('a','9'))
  return 'B' if isprime(flipped) else 'E'
​
def isprime(n):
  for i in range(2,round(math.sqrt(n) + 1)):
    if n % i == 0:
      return False
  return True

