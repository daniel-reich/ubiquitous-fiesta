
def median(nums):
  count = len(nums)
  median = (nums[count//2] + nums[(count-1)//2])/2
  return round(median,1)

