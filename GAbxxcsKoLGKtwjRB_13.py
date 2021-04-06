
def sum_primes(lst):
  mylst = []
  for j in lst:
    if j > 1: 
      isPrime = True
      for i in range(2, j): 
        if (j % i) == 0: 
          isPrime = False
          break
      if isPrime:
        mylst.append(j)
  x = sum(mylst)
  if x == 0:
    return None
  else:
    return x

