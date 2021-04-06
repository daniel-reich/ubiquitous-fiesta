
def mode(nums):
  m = max([nums.count(i) for i in nums])
  return sorted(list(set([i for i in nums if nums.count(i) == m])))

