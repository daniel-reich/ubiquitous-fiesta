
def smith_type(number):
  if is_prime(number):
    return 'Trivial Smith'
  if is_smith(number):
    if is_smith(number+1):
      return 'Youngest Smith'
    elif is_smith(number-1):
      return 'Oldest Smith'
    return 'Single Smith'
  return 'Not a Smith'
    
def is_prime(n):
  return n > 1 and all(n%i for i in range(2,int(n**0.5)+1))
​
def is_smith(n):
  return not is_prime(n) and digital_root(n) == digital_root(sum(get_prime_factors(n)))
  
def digital_root(n):
  while n > 9:
    n = sum(int(i) for i in str(n))
  return n
  
def get_prime_factors(n):
  factors = []
  i = 2
  while n > 1:
    if not n%i:
      while not n%i:
        factors.append(i)
        n //= i
    i += 1
  return factors

