
def is_prime(primes, num, left=0, right=None):
  right = len(primes) - 1
  while left <= right:
    mid_n = (right + left)//2
    if primes[mid_n] == num:
      return 'yes'
    elif primes[mid_n] > num:
      right = mid_n - 1
    else:
      left = mid_n + 1
  else:
    return 'no'

