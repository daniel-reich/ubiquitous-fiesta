
def is_prime(num):
  nums = range(2,10)
  for i in nums:
    if i != num:
      if num%i == 0 or num == 1:
        return False
  return True

