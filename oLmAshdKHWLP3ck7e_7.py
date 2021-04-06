
def min_difference_pair(nums):
  nums.sort()
  result, dif = [nums[0], nums[1]], nums[1] - nums[0]
  for i,j in zip(nums[1:],nums[2:]):
    if j-i < dif or (j-i == dif and j+i < sum(result)):
      result, dif = [i,j], j-i
  return result

