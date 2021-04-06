
def findLargestNum(nums):
  x = -9999
  for i in nums:
    if i > x:
      x = i
  return x

