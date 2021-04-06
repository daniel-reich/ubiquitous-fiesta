
def median(nums):
  l = len(nums)
  if l%2 == 1:
    return nums[l//2]
  else:
    return round(sum(nums[l//2-1:l//2+1])/2,2)

