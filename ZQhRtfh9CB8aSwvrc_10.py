
def greater_than_sum(nums):
  s = nums[0]
  for num in nums[1:]:
    if num <= s:
      return False
    s += num
  return True

