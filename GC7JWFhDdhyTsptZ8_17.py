
def sexy_primes(n, limit):
  primes = list(filter(lambda x: list(filter(lambda y: x % y == 0,range(1,x))) == [1],range(2,limit + 1)))
  lst = []
  for el in primes:
    if el + 6 in primes:
      if n == 2:
        lst.append((el,el+6))
      elif n == 3 and el + 12 in primes:
        lst.append((el,el+6,el+12))
  return lst

