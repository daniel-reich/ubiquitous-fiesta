
def bemirp(n):
  if is_prime(n):
    if rev(n) != n and is_prime(rev(n)):
      if all(is_prime(f(r(n))) for f in (flip,idty) for r in (rev,idty)):
        return 'B'
      return 'E'
    return 'P'
  return 'C'
​
def flip(n):
  s = str(n).translate(str.maketrans('0123456789','01----9-86'))
  return 1 if '-' in s else int(s)
​
def rev(n):
  return int(str(n)[::-1])
  
def idty(n):
  return n
​
def is_prime(n):
  i = 2
  while i*i < n:
    if n%i == 0:
      return False
    i += 1
  return n not in (0,1)

