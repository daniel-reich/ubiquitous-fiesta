
def get_only_evens(nums):
  l = []
  for n in range(0, len(nums)):
    if n % 2 == 0 and nums[n] % 2 == 0:
      l.append(nums[n])
  return l

