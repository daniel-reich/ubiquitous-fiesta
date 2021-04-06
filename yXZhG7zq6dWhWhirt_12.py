
def filter_primes(num):
  primes = []
  for i in range(len(num)):
    ifPrime = True
    for j in range((num[i])):
      if j != 0:
        if float((num[i] / j)) == int((num[i] / j)) and j != num[i] and j != 1:
          ifPrime = False
    if ifPrime == True and num[i] != 1:
      primes.append(num[i])
  return primes

