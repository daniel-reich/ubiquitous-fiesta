
def greater_than_sum(nums):
  s=nums[0]
  for i in range(1,len(nums)):
    if nums[i] <= s:
      return False
    s += nums[i]
  return True

