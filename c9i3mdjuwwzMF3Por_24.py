
def is_prime(n):
  n = int(n)
  if n == 2 or n == 3: return True
  elif n < 2 or n%2 == 0: return False
  elif n < 9: return True
  elif n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True
​
def bemirp(n):
  n, f = str(n), ''.join(k if k in '018' else {'6':'9', '9':'6'}[k] for k in str(n)) if all(int(k) in (0, 1, 6, 8, 9) for k in str(n)) else None
  r, rf = str(n)[::-1], str(f)[::-1] if f else None
  o = 'C'
  if is_prime(n): o = 'P'
  if o == 'P' and is_prime(r) and f and f!=n: o = 'E'
  if o == 'E' and f and is_prime(f) and rf and is_prime(rf): o = 'B'
  return o
​
# The function to check if a number is prime was the hardest part :`D

