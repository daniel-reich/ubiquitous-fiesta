
def duplicate_nums(nums):
  return sorted(set(n for n in nums if nums.count(n) > 1)) or None

