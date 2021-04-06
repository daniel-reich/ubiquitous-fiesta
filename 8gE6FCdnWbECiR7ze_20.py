
def smith_type(number):
  if prime(number):
    return "Trivial Smith"
  dr1 = digital_root(number)
  spf = sum(prime_factors(number))
  dr2 = digital_root(spf)
  if dr1 == dr2:
    if digital_root(number-1) == digital_root(sum([int(i) for i in prime_factors(number-1)])):
      return "Oldest Smith"
    elif digital_root(number+1) == digital_root(sum([int(i) for i in prime_factors(number+1)])):
      return "Youngest Smith"
    else:
      return "Single Smith"
  return "Not a Smith"
  
def prime(n):
  for i in range(2,n):
    if n%i == 0:
      return False
  return n!=1
  
def prime_factors(n):
  lst = []
  for i in range(2,n//2+1):
    if prime(i) and n%i == 0:
      while n%i == 0:
        lst.append(i)
        n = n // i
  return lst
  
def digital_root(n):
  if n < 10:
    return n
  return digital_root(sum([int(i) for i in str(n)]))

