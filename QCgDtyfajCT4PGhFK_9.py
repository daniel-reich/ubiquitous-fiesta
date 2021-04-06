
def prime_factorization(number):
  k = 2
  thislist = list(())
  while number > 1:
    if number%k == 0:
      number = number/k
      thislist.append(k)
    else:
      k += 1
  return thislist

