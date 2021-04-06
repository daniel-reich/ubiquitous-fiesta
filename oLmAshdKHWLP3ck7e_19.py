
def min_difference_pair(nums):
  len1 = len(nums)
  nums.sort()
  result = max(nums)
  final = []
  for i in range(0,len1-1):
    if abs(nums[i+1] - nums[i]) < result:
      result = nums[i+1] - nums[i]
  for i in range (0,len1-1):
    if abs(nums[i+1] - nums[i]) == result:
      final.append(nums[i])
      final.append(nums[i+1])
  return final[:2]

