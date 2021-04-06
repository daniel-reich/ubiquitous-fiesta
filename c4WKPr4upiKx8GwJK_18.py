
def duplicate_nums(nums):
  if len(set(nums)) == len(nums):
    return None
  return sorted([x for x in set(nums) if nums.count(x) > 1])

