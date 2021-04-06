
def median(nums):
  length = len(nums)
  return (sum(nums[length//2-1:length//2+1])/2.0, nums[length//2])[length % 2] if length else None

