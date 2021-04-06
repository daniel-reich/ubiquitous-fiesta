
def is_prime(primes, num):
  low = 0
  high = len(primes) - 1
  while low <= high:
    mid = (low + high) // 2
    guess = primes[mid]
    if guess == num:
      return 'yes'
    elif guess > num:
      high = mid - 1
    else:
      low = mid + 1
  return 'no'

