
def min_difference_pair(nums):
  nums = sorted(nums,reverse=True)
  diff,res = 9999,[]
​
  for i in range(len(nums)-1):
    temp = abs(nums[i]-nums[i+1])
    if temp <= diff:
      diff = temp
      res = [nums[i+1],nums[i]]
  return res

