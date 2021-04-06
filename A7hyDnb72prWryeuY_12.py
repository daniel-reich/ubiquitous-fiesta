
def findLargestNum(nums):
  n=0
  m=nums[n]
  while n<len(nums)-1:
    if m<nums[n+1]:
      m=nums[n+1]
    else:
      pass
    n=n+1
  return m

