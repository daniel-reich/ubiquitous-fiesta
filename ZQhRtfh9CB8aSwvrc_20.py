
def greater_than_sum(nums):
  for i in range(1,len(nums)):
    if not sum(nums[:i:]) < nums[i]:
      return False
  return True

