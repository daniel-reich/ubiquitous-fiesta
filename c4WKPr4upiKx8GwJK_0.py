
def duplicate_nums(nums):
  return sorted([n for i,n in enumerate(nums) if n in nums[i+1:]]) or None

