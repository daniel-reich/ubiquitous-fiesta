
def median(nums):
  median = 0
  if len(nums) % 2 == 0:
    median = (nums[(len(nums) // 2) - 1] + nums[len(nums) // 2]) / 2
  else:
    median = nums[(len(nums) // 2)]
  return median

