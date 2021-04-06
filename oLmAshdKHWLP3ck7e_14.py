
def min_difference_pair(nums):
  nums.sort(reverse=True)
  s = [nums[0], nums[1]]
  for n in range(1, len(nums) - 1):
    if abs(nums[n] - nums[n + 1]) <= abs(s[0] - s[1]):
      s = [nums[n], nums[n + 1]]
  return sorted(s)

