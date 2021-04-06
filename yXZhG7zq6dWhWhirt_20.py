
def filter_primes(lst):
  def is_prime(x):
    y = 2
    if x < y:
      return False
    while y < x:
      if not x % y:
        return False
      y += 1
    return True
  return [x for x in lst if is_prime(x)]

