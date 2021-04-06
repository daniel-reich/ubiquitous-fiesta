
def min_difference_pair(nums):
  nums.sort()
  n=[nums[0],nums[1],abs(nums[1]-nums[0])]
  for i in range(2,len(nums)):
    if abs(nums[i]-nums[i-1]) < n[2]: n=[nums[i-1],nums[i],abs(nums[i-1]-nums[i])]
  return n[:2]

