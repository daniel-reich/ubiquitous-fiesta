
def mode(nums):
  size = max(nums.count(i) for i in set(nums))
  return sorted(i for i in set(nums) if nums.count(i) == size)

