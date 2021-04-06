
def greater_than_sum(nums):
  for x in range(len(nums)):
    if not nums[x]>sum(nums[:x]):
      return False
  return True

