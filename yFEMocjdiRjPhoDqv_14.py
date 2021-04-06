
def prime_in_range(n1, n2):
  nums = list(range(n2))
  for n in range(2, int(n2**0.5) + 1):
    ind = n**2
    while ind < n2:
      nums[ind] = False
      ind += n
  return True if any(nums[n1:]) else False

