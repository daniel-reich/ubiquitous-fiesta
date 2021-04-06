
def mode(nums):
  m = max(nums.count(i) for i in nums)
  return [i for i in sorted(set(nums)) if nums.count(i)==m]

