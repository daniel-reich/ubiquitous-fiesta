
def median(nums):
  nums.sort()
  lenn = len(nums)
  return sum(nums[lenn//2-1+lenn%2:lenn//2+1])/(2-lenn%2)

