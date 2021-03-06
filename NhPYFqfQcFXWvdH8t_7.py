
def extended_euclid_gcd(a, b):
  s = 0; old_s = 1
  t = 1; old_t = 0
  r = b; old_r = a
  while r != 0:
    quotient = old_r//r 
    old_r, r = r, old_r - quotient*r
    old_s, s = s, old_s - quotient*s
    old_t, t = t, old_t - quotient*t
  return old_r, old_s, old_t
​
def mod_inv(n, m):
  for i in range(2,n+1):
    if n%i==0 and m%i==0:
      return False
  gcd, x, y = extended_euclid_gcd(n, m)
  if x < 0:
    x += m
  return x

