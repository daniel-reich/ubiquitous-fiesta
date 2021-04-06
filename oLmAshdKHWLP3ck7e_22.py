
def min_difference_pair(nums):
  pair = [nums[0], nums[1]]
  d = abs(nums[0] - nums[1])
  for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
      n = abs(nums[i] - nums[j])
      if n < d:
        d = n
        pair = [nums[i], nums[j]]
      if n == d and sum(pair) > (nums[i] + nums[j]):
        d = n
        pair = [nums[i], nums[j]]
  return sorted(pair)

