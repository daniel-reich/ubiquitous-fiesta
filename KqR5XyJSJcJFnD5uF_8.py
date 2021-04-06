
def median(nums):
  return nums[len(nums)//2] if len(nums)%2 else (nums[len(nums)//2-1]+nums[len(nums)//2])/2

