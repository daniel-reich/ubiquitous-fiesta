
def greater_than_sum(nums):
  for i in range(1,len(nums)):
    if nums[i]>sum(nums[:i]):
      continue
    else:
      return False
  return True

