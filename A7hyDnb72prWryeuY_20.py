
def findLargestNum(nums):
  max = 0
  for a in nums:
    if a > max:
      max = a
  
  return max

