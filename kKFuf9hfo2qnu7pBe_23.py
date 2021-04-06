
def is_prime(primes, num, left=0, right=None):
  if right == None:
    right = len(primes) - 1
​
  if left > right:
    return "no"
​
  mid = left + (right - left) // 2
  if primes[mid] > num:
    return is_prime(primes, num, left, mid - 1)
  elif primes[mid] < num:
    return is_prime(primes, num, mid + 1, right)
  else:
    return "yes"

