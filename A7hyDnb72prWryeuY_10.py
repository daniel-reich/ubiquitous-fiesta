
def findLargestNum(nums):
  num = 0
  for i in nums:
    if i > num:
      num = i
  return num

