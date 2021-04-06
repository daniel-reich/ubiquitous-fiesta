
def is_prime(primes, num, left=0, right=None):
  right = len(primes)-1
  while right >= left:
    guess = int((left+right)/2)
    if primes[guess]==num:
      return "yes"
    if primes[guess]<num:
      left = guess+1
    else:
      right = guess-1
  
  return "no"

