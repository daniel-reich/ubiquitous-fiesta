
def min_difference_pair(nums):
  nums=sorted(nums)
  dif=[x-y for x,y in zip(nums[1:], nums)]
  ind=[dif.index(i) for i in dif if i==min(dif)][0]
  return [nums[ind],nums[ind+1]]

