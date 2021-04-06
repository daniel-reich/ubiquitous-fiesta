
def primes_below_num(n):
  def is_prime(m):
    if m >= 2:
      for y in range(2, m):
        if not (m % y):
          return False
    else:
      return False
    return True
  nums = []
  for i in range(n+1):
    nums.append(i)
  def filter_primes(nums):
    return list(filter(is_prime, nums))
  return filter_primes(nums)

