
def sum_primes(lst):
  sums = []
  emtyd = [] 
  if lst == emtyd:
    return None
  for i in lst:
    for x in range(2, i):
      if i % x == 0:
        break
    else:
      if i != 1:
        sums.append(i)
  a = 0
  for n in sums:
    a += n
  return a

