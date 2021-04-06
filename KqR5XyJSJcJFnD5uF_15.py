
def median(nums):
  return round((nums[int(len(nums)/2)-1]+nums[int(len(nums)/2)])/2,1) if len(nums)%2==0 else nums[int((len(nums)+1)/2)-1]

