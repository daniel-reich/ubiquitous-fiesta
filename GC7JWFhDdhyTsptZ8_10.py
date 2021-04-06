
def sexy_primes(n, limit):
  pairs = []
  for i in range(2, limit-((n-1)*6)):
    num_is_prime = True
    next_is_prime = True
    for y in range(2, int(round(i**(0.5)))+1):
      if i/y == i//y:
        num_is_prime = False
        break
    if num_is_prime:
      nex = i+6
      for y in range(2, int(round(nex**(0.5)))+1):
        if nex/y == nex//y:
          next_is_prime = False
          break
    if next_is_prime and n == 3:
      nexy = i+12
      for y in range(2, int(round(nexy**(0.5)))+1):
        if nexy/y == nexy//y:
          next_is_prime = False
          break
    if next_is_prime and num_is_prime:
      if n == 2:
        pairs.append((i, nex))
      if n == 3:
        pairs.append((i, nex, nexy))
  return pairs

