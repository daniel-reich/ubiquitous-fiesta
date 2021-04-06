
def is_prime(primes, num, left=0, right=None):
  right = len(primes) - 1
  print(left)
  print(right)
  while left <= right:
    mid = (left + right) // 2
    print(mid)
    if primes[mid] == num:
      return 'yes'
    elif primes[mid] > num:
      print('mid was greater than num')
      right = mid - 1
    else:
      print('mid was less than num')
      left = mid + 1
  return 'no'

