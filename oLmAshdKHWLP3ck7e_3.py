
def min_difference_pair(nums):
  nums = sorted(nums)
  return sorted([[x,y] for x,y in zip(nums,nums[1:])], key = lambda x: x[1]-x[0])[0]

