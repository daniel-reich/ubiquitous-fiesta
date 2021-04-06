
def sexy_primes(n, limit):
  l = []
  l1 = []
  for i in range(limit+1):
    k = 0
    for y in range(1,i+1):
      if i%y == 0:
        k += 1
    if k == 2:
      l.append(i)
  for i in l:
    if n == 2:
      if i + 6 in l:
        l1.append((i,i+6))
    if n == 3:
      if i+6 in l and i+12 in l:
        l1.append((i,i+6,i+12))
  return l1

