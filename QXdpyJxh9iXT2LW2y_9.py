
def primes(n):
  if n < 4:
    return []
  p = [2]
  for i in range(3, n//2):
    if 2*i == n: break
    for j in p:
      if i%j == 0:
        break
    else:
      p.append(i)
  return p
  
def semiprimes(n):
  p = primes(n)
  semi = set()
  semi_not_root = set()
  for i in p:
    for j in p:
      prod = i*j
      if prod >= n: break
      semi.add(prod)
      if i != j:
        semi_not_root.add(prod)
  return sorted(semi), sorted(semi_not_root)

