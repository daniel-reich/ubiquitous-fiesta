
def is_prime (primes, x):
  def binarySearch(arr, l, r, x):
    if r >= l: 
      mid = l + (r - l) // 2
      if arr[mid] == x: 
        return True
      elif arr[mid] > x: 
        return binarySearch(arr, l, mid-1, x) 
      else: 
        return binarySearch(arr, mid + 1, r, x) 
    else: 
      return False
  return "yes" if binarySearch(primes, 0, len(primes), x) else "no"

