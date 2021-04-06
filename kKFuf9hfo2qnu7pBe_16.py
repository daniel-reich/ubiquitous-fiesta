
def is_prime(primes, num, left=0, right=None):
  m=len(primes[left:right])//2+left
  if primes[m]==num:
    return "yes"
  elif left==m:
    return "no"
  elif primes[m]>num:
    return is_prime(primes,num,left,m)
  else:
    return is_prime(primes,num,m,right)

