
def max_total(nums):
  nums.sort()
  return sum(nums[-5:])

