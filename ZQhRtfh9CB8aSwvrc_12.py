
def greater_than_sum(nums):
  for n in range(1, len(nums)):
    if nums[n] <= sum(nums[:n]):
      return False
      
  return True

