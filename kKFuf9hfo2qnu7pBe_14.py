
def is_prime(primes, num):
  low = 0
  high = len(primes) - 1
  while low <= high:
    mid = (low + high) // 2
    if primes[mid] == num:
      return 'yes'
    elif primes[mid] > num:
      high = mid - 1
    else:
      low = mid + 1
  return 'no'

