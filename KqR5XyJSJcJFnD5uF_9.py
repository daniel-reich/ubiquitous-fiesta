
def median(nums):
  nums.sort()
  if len(nums)%2==0:
    return round((nums[len(nums)//2-1]+nums[len(nums)//2])/2,1)
  else:
    return nums[len(nums)//2]

