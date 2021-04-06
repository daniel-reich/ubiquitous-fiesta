
def min_difference_pair(nums):
  nums=sorted(nums)
  ans = nums[0:2]
  for i in range(2,len(nums)):
    if ans[1]-ans[0] > nums[i]-nums[i-1]:
      ans = nums[i-1:i+1]
  return ans

