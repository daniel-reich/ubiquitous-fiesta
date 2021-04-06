
def median(nums):
  if len(nums)%2!=0:
    return nums[len(nums)//2]
  else:
    s=nums[len(nums)//2] + nums[(len(nums)//2)-1]
    return round(s/2,1)

