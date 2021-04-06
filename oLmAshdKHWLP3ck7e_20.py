
def min_difference_pair(nums):
  nums.sort()
  w = 1000
  l = []
  for i in range(len(nums)-1):
    if abs(nums[i]-nums[i+1])<w:
      l = [nums[i],nums[i+1]]
      w = abs(nums[i]-nums[i+1])
  return l

