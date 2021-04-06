
def min_difference_pair(nums):
  d = {}
  for i in range(len(nums)):
    for j in range(len(nums)):
      if i != j:
        diff = abs(nums[i] - nums[j])
        if diff in d:
          if nums[i] + nums[j] < sum(d[diff]):
            d[diff] =[nums[i],nums[j]]
          else:
            pass
        else:
          d[diff] =[nums[i],nums[j]]
  final = d[min(d)]
  return sorted(final)

