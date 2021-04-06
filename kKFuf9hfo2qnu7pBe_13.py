
def is_prime(primes, num, left=0, right=None):
  low = left
  high = len(primes) - 1
  while low <= high:
    middle = (low + high) // 2
    if primes[middle] == num:
      if num%2 ==1:
        return 'yes'
    elif primes[middle] < num:
      low = middle + 1
    else:
      high = middle - 1
  return 'no'

