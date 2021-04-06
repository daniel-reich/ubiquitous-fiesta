
def is_prime(primes, num, left=0, right=None):
  #binary search middle first then see if bigger or smaller than middle 
  end = len(primes) - 1 
  start = 0
  while start <= end:
    mid = (start + end) //2 
    item = primes[mid]
    if num == item:
      return 'yes'
    if num < item:
      end = mid - 1
    else:
      start = mid + 1
  return 'no'

