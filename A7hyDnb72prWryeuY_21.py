
def findLargestNum(nums):
  if len(nums) == 0:
    return False
  largest = nums[0]
  for item in nums:
    if item > largest:
      largest = item
  return largest

