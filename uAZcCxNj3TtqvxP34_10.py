
def mode(nums):
  counts = [nums.count(n) for n in nums]
  return [n for n in sorted(set(nums)) if nums.count(n) == max(counts)]

