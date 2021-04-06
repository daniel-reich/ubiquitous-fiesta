
def max_total(nums):
  nums.sort()
  nums.reverse()
  total = 0
  for i in range(5):
    total += nums[i]
  return total

