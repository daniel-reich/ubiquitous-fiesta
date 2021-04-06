
def prime_factors(n):
  """ Return a list with the prime factors of n """
  ### Function needed for simplify_root()
  ### Function needed for is_economical()
  i = 2
  while n>1:
    while not n%i:
      n//=i
      yield i
    i+=1
​
def is_economical(n):                   # Economical numbers
  """ View rules on edabit """
  prime_fac = list(prime_factors(n))
  prime_fac = list(set([(x, prime_fac.count(x)) for x in prime_fac]))
  sum_prime = sum(len(str(x[0])) if x[1]==1 else len(str(x[0])) + len(str(x[1])) for x in prime_fac)
  return "Equidigital" if sum_prime == len(str(n)) else "Frugal" if sum_prime < len(str(n)) else "Wasteful"

